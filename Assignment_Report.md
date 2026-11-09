# NeuroPulse — Rule-Based GPU Health and Efficiency Advisor
Assignment 2.3 | Roderick Austin | November 9, 2026

## 1. Three initial project ideas

**NeuroPulse: GPU Health and Efficiency Advisor.** Accepts GPU sample measurements and flags conditions for review. IF temperature reaches an illustrative threshold, THEN recommend thermal review; IF utilization is low while relative power is high, THEN recommend investigating background work. Potential value: making resource use understandable to developers and operators.

**Cybersecurity Alert Triage Assistant.** Accepts simulated failed-login counts, privileged-account status, and unfamiliar-device flags. IF repeated failures exceed a policy threshold, THEN flag investigation; IF an unfamiliar device accesses a privileged account, THEN recommend verification. Potential value: consistent first-pass triage for smaller IT teams.

**Data-Center Workload Scheduling Advisor.** Accepts queue urgency, capacity availability, and a manually entered electricity-cost category. IF work is deferrable and cost is high, THEN recommend postponement; IF work is urgent and capacity is available, THEN recommend running it. Potential value: helping operators reason about scheduling and cost trade-offs.

**Selected project:** I selected NeuroPulse because it connects my coursework to a project I am already developing and to my interest in computing efficiency. A small advisor provides a clear way to demonstrate IF-THEN reasoning and explain every output. This classroom prototype introduces the concept without presenting it as the complete product or evidence of measured savings.

## 2. Rules and implementation

All numeric thresholds are illustrative classroom policy values, not manufacturer specifications, universal safe operating limits, or validated tuning recommendations. Inputs are manually entered sample data; the program does not access or control a GPU.

1. Reject nonfinite numbers, negative temperature or power, utilization outside 0–100%, and reference power <= 0. Reprompt for nonnumeric input.
2. Calculate relative power = power draw / reference power. The reference is user-entered, not a detected hardware rating.
3. IF temperature >= 80 C, THEN THERMAL_REVIEW. Highest priority.
4. ELIF utilization < 20% AND relative power >= 0.50, THEN EFFICIENCY_REVIEW.
5. ELIF utilization >= 80%, THEN HIGH_ACTIVITY.
6. ELSE output NO_RULE_TRIGGERED. This does not certify hardware health or optimal efficiency.
7. Ask whether to evaluate another sample. Continue only for y; handle end-of-input or interruption cleanly.

Implementation: `advise()` validates input and evaluates ordered rules; `read_number()` handles numeric entry; `main()` manages user interaction. Only Python standard-library modules are used.

## 3. AI collaboration

The initial draft used a computer troubleshooting idea. I asked for ideas with potential impact on the technology industry and specifically requested NeuroPulse as one of the three. I then selected NeuroPulse and authorized building the classroom prototype. The AI assistant helped define rules, implement the program, and check its outputs. The earlier troubleshooting files are superseded.

## 4. Test results

All measurements are invented test inputs. Each row shows temperature (C), utilization (%), power (W), reference power (W), and actual rule output.

| Test | Temperature | Utilization | Power | Reference | Actual result | Status |
|---|---:|---:|---:|---:|---|---|
| 1 | 85 | 95 | 240 | 300 | THERMAL_REVIEW | PASS |
| 2 | 55 | 10 | 180 | 300 | EFFICIENCY_REVIEW | PASS |
| 3 | 65 | 90 | 200 | 300 | HIGH_ACTIVITY | PASS |
| 4 | 60 | 45 | 100 | 300 | NO_RULE_TRIGGERED | PASS |

Actual responses:
- **THERMAL_REVIEW:** Review cooling and workload; consult device specifications.
- **EFFICIENCY_REVIEW:** Low utilization with high relative power; investigate background work.
- **HIGH_ACTIVITY:** High utilization; compare performance and power over time.
- **NO_RULE_TRIGGERED:** No demonstration threshold matched; continue monitoring.

Additional automated verification: nine valid cases check rules, boundaries, and priority; eight invalid cases check ranges, NaN, and infinity. Two test methods cover 17 subcases. Interactive checks cover malformed input and repeat/exit behavior.

**Limitations:** A single sample cannot establish efficiency, performance preservation, or a fault. Low utilization may have legitimate causes. There is no hardware-specific calibration, live telemetry, learning, or optimization control. Advice prompts review, not diagnosis.

## 5. Reflection (draft for student review)

This project demonstrates how a small part of the NeuroPulse concept can be expressed through traditional rule-based AI. The program accepts manually entered GPU temperature, utilization, power draw, and a reference power value. It validates those numbers, calculates power relative to the reference, and evaluates a fixed sequence of conditions. Each output identifies the rule that triggered, making the recommendation easy to trace. The program does not train a model or change hardware settings.

I chose NeuroPulse because it connects this assignment to an existing project I am developing. To be transparent, the classroom program is a separate educational prototype rather than the complete NeuroPulse product. Its examples use invented measurements, so successful tests demonstrate correct rule execution, not verified energy savings or real hardware performance.

Working with the AI assistant highlighted two design challenges. First, the initial assignment draft focused on general computer troubleshooting, which did not reflect the direction I wanted. I redirected the brainstorming toward technology industry problems and selected NeuroPulse. This showed me that giving the assistant a clear purpose and personal context matters as much as requesting working code.

Second, the rules needed precise boundaries and priorities. A sample could have both a high temperature and low utilization with high relative power. The design resolves that overlap by checking the temperature rule first. Explicit comparison operators also clarify what happens at exactly 80 degrees, 20 percent utilization, or half the reference power. These thresholds are demonstration choices rather than universal hardware limits.

The tests check ordinary examples, boundary conditions, competing rules, and invalid inputs. Compared with machine learning, this system is predictable and explainable, but it cannot discover patterns or adapt without a programmer changing its rules. A learned model could potentially account for workload history and more complex relationships. This project helps me understand both the usefulness and the limits of starting with transparent, manually defined decisions.
