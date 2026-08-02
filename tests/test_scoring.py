import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from belgium_pulse.scoring import chaos_score, temperature_stress


class ChaosScoreTests(unittest.TestCase):
    def test_comfortable_conditions_are_low_pressure(self):
        score = chaos_score(
            apparent_temperature_c=18,
            precipitation_probability_pct=0,
            wind_speed_kmh=0,
            european_aqi=0,
        )
        self.assertEqual(score, 0.0)

    def test_score_is_capped(self):
        score = chaos_score(
            apparent_temperature_c=80,
            precipitation_probability_pct=500,
            wind_speed_kmh=500,
            european_aqi=500,
        )
        self.assertEqual(score, 100.0)

    def test_temperature_stress_is_symmetric(self):
        self.assertEqual(temperature_stress(10), temperature_stress(26))


if __name__ == "__main__":
    unittest.main()

