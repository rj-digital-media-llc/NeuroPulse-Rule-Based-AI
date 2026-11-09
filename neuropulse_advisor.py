"""NeuroPulse educational advisor: manual sample data, fixed rules, no controls."""
import math

# Demonstration policy values, not manufacturer limits or validated tuning advice.
TEMP_REVIEW_C = 80.0
LOW_UTIL_PERCENT = 20.0
HIGH_POWER_RATIO = 0.50
HIGH_UTIL_PERCENT = 80.0


def advise(temperature, utilization, power, reference_power):
    """Return the first matching rule; reference_power is a user-set comparison."""
    values = (temperature, utilization, power, reference_power)
    if not all(math.isfinite(v) for v in values):
        raise ValueError("All measurements must be finite numbers.")
    if temperature < 0 or not 0 <= utilization <= 100 or power < 0 or reference_power <= 0:
        raise ValueError("Use temperature >= 0, utilization 0-100, power >= 0, reference > 0.")
    ratio = power / reference_power
    # Thermal review comes first, even when another rule also matches.
    if temperature >= TEMP_REVIEW_C:
        return "THERMAL_REVIEW: Review cooling and workload; consult device specifications."
    elif utilization < LOW_UTIL_PERCENT and ratio >= HIGH_POWER_RATIO:
        return "EFFICIENCY_REVIEW: Low utilization with high relative power; investigate background work."
    elif utilization >= HIGH_UTIL_PERCENT:
        return "HIGH_ACTIVITY: High utilization; compare performance and power over time."
    else:
        return "NO_RULE_TRIGGERED: No demonstration threshold matched; continue monitoring."


def read_number(prompt):
    """Reprompt for malformed or nonfinite numeric input."""
    while True:
        try:
            value = float(input(prompt))
            if not math.isfinite(value):
                raise ValueError
            return value
        except ValueError:
            print("Enter a finite number, such as 65 or 120.5.")


def main():
    print("NeuroPulse | Rule-Based GPU Health and Efficiency Advisor")
    print("Educational sample data only. No hardware access or setting changes.")
    print("Thresholds are illustrative, not manufacturer limits or proof of savings.")
    try:
        while True:
            temperature = read_number("Temperature (C): ")
            utilization = read_number("Utilization (%): ")
            power = read_number("Power draw (W): ")
            reference = read_number("Reference power for comparison (W): ")
            try:
                print(advise(temperature, utilization, power, reference))
            except ValueError as error:
                print("Invalid sample:", error)
            if input("Evaluate another sample? (y/n): ").strip().lower() != "y":
                break
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")


if __name__ == "__main__":
    main()
