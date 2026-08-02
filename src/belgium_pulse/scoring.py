"""Small, testable scoring functions used by the ingestion pipeline."""

from __future__ import annotations


def clamp(value: float, lower: float = 0.0, upper: float = 100.0) -> float:
    """Keep a value inside an inclusive range."""
    return max(lower, min(value, upper))


def temperature_stress(apparent_temperature_c: float) -> float:
    """Score discomfort around a comfortable apparent temperature of 18°C."""
    return clamp(abs(apparent_temperature_c - 18.0) * 5.0)


def chaos_score(
    *,
    apparent_temperature_c: float,
    precipitation_probability_pct: float,
    wind_speed_kmh: float,
    european_aqi: float,
) -> float:
    """Return an explainable 0–100 city-pressure score."""
    score = (
        0.45 * clamp(european_aqi)
        + 0.20 * temperature_stress(apparent_temperature_c)
        + 0.15 * clamp(precipitation_probability_pct)
        + 0.20 * clamp(wind_speed_kmh * 2.0)
    )
    return round(clamp(score), 1)

