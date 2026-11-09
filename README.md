# NeuroPulse: Rule-Based GPU Health and Efficiency Advisor

Educational prototype inspired by an existing NeuroPulse project. It uses **manual sample measurements and explicit rules**, with no machine learning, hardware access, or hardware setting changes. All thresholds are illustrative classroom values, not manufacturer limits or proof of energy savings.

## Files

- [Assignment_Report.md](Assignment_Report.md) — three project ideas, selection rationale, IF–THEN rules, four test results, AI collaboration, and a reflection draft for student review
- [neuropulse_advisor.py](neuropulse_advisor.py) — interactive Python rule engine
- [test_neuropulse_advisor.py](test_neuropulse_advisor.py) — automated boundary and validation tests
- [requirements.txt](requirements.txt) — Python requirements (standard library only)

## Run

Python 3.10 or newer. No third-party packages needed.

```bash
python neuropulse_advisor.py
python -m unittest -v
```

Enter temperature in Celsius, GPU utilization percentage, power draw in watts, and a **manually chosen** reference power in watts. The program returns the first applicable recommendation.

## Rule priority

1. Validate finite numeric values, utilization between 0 and 100, nonnegative temperature/power, and positive reference power.
2. If temperature >= 80°C, flag **THERMAL_REVIEW**.
3. Else if utilization < 20% and power/reference >= 0.50, flag **EFFICIENCY_REVIEW**.
4. Else if utilization >= 80%, flag **HIGH_ACTIVITY**.
5. Otherwise return **NO_RULE_TRIGGERED**.

## Sample results

| Temperature °C | Utilization | Power W | Reference W | Result |
|---:|---:|---:|---:|---|
| 85 | 95% | 240 | 300 | THERMAL_REVIEW |
| 55 | 10% | 180 | 300 | EFFICIENCY_REVIEW |
| 65 | 90% | 200 | 300 | HIGH_ACTIVITY |
| 60 | 45% | 100 | 300 | NO_RULE_TRIGGERED |

The automated suite covers 17 valid and invalid subcases. These are invented examples, not hardware benchmarks.

## Transparency

Created with AI assistance for Full Sail University's rule-based AI assignment. This repository is a standalone classroom demonstration, **not the full commercial NeuroPulse system**. It does not measure real GPU efficiency or perform optimization. Review the reflection draft in the report before submitting it as your own account of the experience.
