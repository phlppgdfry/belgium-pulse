import unittest
from demo import domain


class CityScenarioTests(unittest.TestCase):
    def test_contributions_match_score_with_rounding_tolerance(self):
        for r in domain.seed():
            self.assertAlmostEqual(
                sum(domain.contributions(r).values()), domain.score(r), delta=0.051
            )

    def test_extremes_and_restore(self):
        r = domain.seed()[0]
        p = dict(id=r["id"], action="scenario", temperature=60, rain=100, wind=200, aqi=500)
        updated = domain.execute([r], p)
        self.assertEqual(domain.score(updated), 100)
        restored = domain.execute([updated], dict(id=r["id"], action="restore"))
        self.assertEqual(restored, r)

    def test_invalid_values_are_rejected(self):
        r = domain.seed()[0]
        for invalid in [float("nan"), float("inf"), True, 101, -1, 10**400]:
            with self.assertRaises(ValueError):
                domain.execute(
                    [r],
                    dict(
                        id=r["id"], action="scenario", temperature=18, rain=invalid, wind=10, aqi=20
                    ),
                )
