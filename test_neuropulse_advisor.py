"""Boundary, precedence, and validation checks using only the standard library."""
import unittest
from neuropulse_advisor import advise


class AdvisorTests(unittest.TestCase):
    def test_rules_and_boundaries(self):
        cases = [
            ((85, 95, 240, 300), "THERMAL_REVIEW"),
            ((80, 10, 180, 300), "THERMAL_REVIEW"),
            ((79.9, 10, 180, 300), "EFFICIENCY_REVIEW"),
            ((55, 19.9, 150, 300), "EFFICIENCY_REVIEW"),
            ((55, 20, 150, 300), "NO_RULE_TRIGGERED"),
            ((55, 10, 149.9, 300), "NO_RULE_TRIGGERED"),
            ((65, 80, 200, 300), "HIGH_ACTIVITY"),
            ((65, 79.9, 200, 300), "NO_RULE_TRIGGERED"),
            ((60, 45, 100, 300), "NO_RULE_TRIGGERED"),
        ]
        for sample, expected in cases:
            with self.subTest(sample=sample):
                self.assertTrue(advise(*sample).startswith(expected + ":"))

    def test_invalid_samples(self):
        cases = [(-1, 20, 100, 300), (60, -1, 100, 300),
                 (60, 101, 100, 300), (60, 20, -1, 300),
                 (60, 20, 100, 0), (60, 20, 100, -1),
                 (float("nan"), 20, 100, 300),
                 (60, 20, float("inf"), 300)]
        for sample in cases:
            with self.subTest(sample=sample), self.assertRaises(ValueError):
                advise(*sample)


if __name__ == "__main__":
    unittest.main()
