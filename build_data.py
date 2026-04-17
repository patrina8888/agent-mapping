#!/usr/bin/env python3
"""Parse the AI Agent TAM CSV and emit a data.js file for the viz page."""
import csv
import json
import re
import os

SRC_PATH = "/Users/patrinafan/Downloads/AI_Agent_TAM_2026-04 (1).xlsx"
SHEET = "All Tracks — Labor vs SW TAM"
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.js")

CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩"

def parse_tam(val):
    if not val:
        return 0
    m = re.search(r'\$?\s*([\d.]+)\s*B', val)
    if m:
        return float(m.group(1))
    return 0

def parse_rate(val):
    if not val:
        return 0
    nums = re.findall(r'[\d.]+', val)
    if len(nums) >= 2:
        return (float(nums[0]) + float(nums[1])) / 2
    if len(nums) == 1:
        return float(nums[0])
    return 0

def parse_ratio(val):
    if not val:
        return 0
    m = re.search(r'([\d.]+)\s*x', val)
    if m:
        return float(m.group(1))
    return 0

rows = []
current_cat_icon = ""
current_cat_name = ""

import openpyxl
wb = openpyxl.load_workbook(SRC_PATH, data_only=True)
ws = wb[SHEET]

def iter_rows():
    for row in ws.iter_rows(values_only=True):
        yield ["" if v is None else str(v) for v in row]

for raw in iter_rows():
        if not raw:
            continue
        first = (raw[0] or "").strip()
        if not first:
            continue

        # Category header row like "①  Personal Consumer & Household"
        if first[0] in CIRCLED:
            current_cat_icon = first[0]
            current_cat_name = first[1:].strip()
            continue

        # Data row: first cell is a pure integer
        if not first.isdigit():
            continue

        def col(i):
            return raw[i].strip() if len(raw) > i else ""

        sub_track = col(2)
        sw_tam_str = col(3)
        labor_tam_str = col(4)
        impact_type = col(5)
        disp_rate = col(6)
        net_effect = col(7)
        description = col(8)
        companies = col(9)
        funding = col(10)
        insights = col(11)
        valuation_tier = col(12)
        public_status = col(13)
        ratio_str = col(14)

        category = col(1) or current_cat_name

        rows.append({
            "id": len(rows) + 1,
            "num": int(first),
            "categoryIcon": current_cat_icon,
            "category": category,
            "subTrack": sub_track,
            "swTam": parse_tam(sw_tam_str),
            "swTamStr": sw_tam_str,
            "laborTam": parse_tam(labor_tam_str),
            "laborTamStr": labor_tam_str,
            "impactType": impact_type,
            "displacementRate": parse_rate(disp_rate),
            "displacementRateStr": disp_rate,
            "netEffect": net_effect,
            "description": description,
            "companies": companies,
            "funding": funding,
            "insights": insights,
            "valuationTier": valuation_tier,
            "publicStatus": public_status,
            "laborSwRatio": parse_ratio(ratio_str),
            "laborSwRatioStr": ratio_str,
        })

print(f"Parsed {len(rows)} rows")
cats = {}
for r in rows:
    key = r["categoryIcon"] + " " + r["category"]
    cats[key] = cats.get(key, 0) + 1
for k, v in cats.items():
    print(f"  {k}: {v}")

total_sw = sum(r["swTam"] for r in rows)
total_labor = sum(r["laborTam"] for r in rows)
print(f"Total SW TAM:    ${total_sw:,.1f}B")
print(f"Total Labor TAM: ${total_labor:,.1f}B")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("// Auto-generated from AI_Agent_TAM.xlsx - All Tracks CSV\n")
    f.write("window.TAM_DATA = ")
    f.write(json.dumps(rows, ensure_ascii=False, indent=1))
    f.write(";\n")

print(f"Wrote {OUT_PATH}")
