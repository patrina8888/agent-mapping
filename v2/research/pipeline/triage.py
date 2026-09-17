#!/usr/bin/env python3
"""
Investability-Triage Score (ITS) — reference implementation for v3_pipeline_spec.md (§C).
Ranks every v2 track (and any provisional white cell) for HTC seed/A investability.
Fully reproducible: every input is a field already in v2_master.json.

  ITS_base = 20 * (0.34*E + 0.12*S + 0.16*K + 0.24*W + 0.14*Rc)     # 0-100
  ITS      = ITS_base * chasm(conv)     chasm = {High:1.0, Medium:0.85, Low:0.65}

  E  reachable capture-EXPANSION headroom = (ceiling(V) - current) * readiness, /32 *5 ; additive *0.5
  S  labor-TAM size = log10(labor_b) scaled 2..2000 -> 0..5   (lowest weight: dollar-size is a trap)
  K  capability-readiness = readiness*5  (verifiability-gated, hardware-timeline-discounted)
  W  seed/A door-open = 5 - L  (lab/incumbent-capture inverse; * moat-ownership modifier, neutral in batch)
  Rc near-term reg-gate clearance = 5 - R

  readiness = (V/5) * (1 - 0.18*P) * (0.6 + 0.10*H)     # physicality collapses it (hardware clock)
"""
import json, re, math, csv, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(HERE, "..", "v2_master.json")

CEIL = {0: 3, 1: 5, 2: 8, 3: 12, 4: 20, 5: 32}   # verifiability -> achievable capture ceiling %
CHASM = {"High": 1.00, "Medium": 0.85, "Low": 0.65}
WEIGHTS = dict(E=0.34, S=0.12, K=0.16, W=0.24, Rc=0.14)


def parse_capture(s, ceil):
    """Current realized labor-capture %, guarded to [0, ceil]. Net-new/additive -> ~1%."""
    if not s or s == "None":
        return 1.0
    low = s.lower()
    if low.startswith("n/a") or "no single clean rate" in low or "bifurcated" in low:
        return 1.0
    m = re.match(r"\s*<?\s*~?\s*(\d+\.?\d*)\s*[–-]?\s*(\d+\.?\d*)?\s*%", s)
    if m:
        a = float(m.group(1)); b = float(m.group(2)) if m.group(2) else a
        val = a * 0.7 if "<" in s[: s.find("%") + 1] else (a + b) / 2
        return max(0.0, min(val, ceil))
    return 1.0


def score(t, moat_modifier=1.0):
    V, H, P, R, L, D = t["V"], t["H"], t["P"], t["R"], t["L"], t["D"]
    lb = float(t["labor_b"]); coupled = t["coupled"]; conv = t["conv"]
    ceil = CEIL[V]
    cur = parse_capture(t.get("capture"), ceil)

    readiness = (V / 5) * max(0.10, 1 - 0.18 * P) * (0.6 + 0.10 * H)   # 0..1
    reach_head = max(0.0, ceil - cur) * readiness
    E = 5 * reach_head / 32
    if not coupled:
        E *= 0.5                                   # augment: seat-ARR expansion, not labor capture

    S = max(0.0, min(5.0, (math.log10(lb) - math.log10(2)) /
                     (math.log10(2000) - math.log10(2)) * 5))
    K = readiness * 5
    W = max(0.0, min(5.0, (5 - L) * moat_modifier))
    Rc = 5 - R

    base = 20 * (WEIGHTS["E"] * E + WEIGHTS["S"] * S + WEIGHTS["K"] * K +
                 WEIGHTS["W"] * W + WEIGHTS["Rc"] * Rc)
    its = base * CHASM.get(conv, 0.85)
    return dict(id=t["id"], its=round(its, 1), E=round(E, 2), S=round(S, 2),
                K=round(K, 2), W=round(W, 2), Rc=Rc, readiness=round(readiness, 2),
                ceiling=ceil, current=round(cur, 1), coupled=coupled, conv=conv,
                net=t["net"], labor_b=lb, VHPRLD=f"{V}{H}{P}{R}{L}{D}")


def main():
    data = json.load(open(MASTER))
    rows = sorted((score(t) for t in data), key=lambda r: -r["its"])
    out = os.path.join(HERE, "its_ranked.csv")
    cols = ["id", "its", "E", "S", "K", "W", "Rc", "readiness", "ceiling",
            "current", "coupled", "conv", "net", "labor_b", "VHPRLD"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"scored {len(rows)} rows -> {out}")
    for r in rows[:20]:
        print(f"  {r['id']:6} ITS={r['its']:>5}  E={r['E']:>4} S={r['S']:>4} "
              f"K={r['K']:>4} W={r['W']:>4} Rc={r['Rc']}  {r['conv']:>6} {r['net']}")


if __name__ == "__main__":
    main()
