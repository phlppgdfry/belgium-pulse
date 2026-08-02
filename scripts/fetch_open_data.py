#!/usr/bin/env python3
"""Fetch a small live Belgium Pulse snapshot from public Open-Meteo endpoints."""

from __future__ import annotations

import csv
import json
import ssl
import sys
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

import certifi

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from belgium_pulse.scoring import chaos_score  # noqa: E402

CITIES = {
    "Brussel": (50.8503, 4.3517),
    "Antwerpen": (51.2194, 4.4025),
    "Gent": (51.0543, 3.7174),
    "Luik": (50.6326, 5.5797),
    "Charleroi": (50.4108, 4.4446),
}
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
AIR_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "city_hourly.csv"
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


def get_json(url: str, params: dict[str, str]) -> dict:
    request_url = f"{url}?{urlencode(params)}"
    with urlopen(request_url, timeout=20, context=SSL_CONTEXT) as response:  # noqa: S310 - fixed HTTPS hosts
        return json.load(response)


def fetch_city(city: str, latitude: float, longitude: float) -> dict[str, object]:
    common = {"latitude": str(latitude), "longitude": str(longitude), "timezone": "UTC"}
    weather = get_json(
        WEATHER_URL,
        common
        | {
            "current": "temperature_2m,apparent_temperature,wind_speed_10m",
            "hourly": "precipitation_probability",
            "forecast_days": "1",
        },
    )
    air = get_json(AIR_URL, common | {"current": "pm10,pm2_5,european_aqi"})
    current = weather["current"]
    air_current = air["current"]
    precipitation_probability = weather["hourly"]["precipitation_probability"][0]
    score = chaos_score(
        apparent_temperature_c=current["apparent_temperature"],
        precipitation_probability_pct=precipitation_probability,
        wind_speed_kmh=current["wind_speed_10m"],
        european_aqi=air_current["european_aqi"],
    )
    return {
        "observed_at_utc": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "temperature_c": current["temperature_2m"],
        "apparent_temperature_c": current["apparent_temperature"],
        "precipitation_probability_pct": precipitation_probability,
        "wind_speed_kmh": current["wind_speed_10m"],
        "pm10": air_current["pm10"],
        "pm2_5": air_current["pm2_5"],
        "european_aqi": air_current["european_aqi"],
        "chaos_score": score,
    }


def main() -> None:
    rows = [fetch_city(city, *coordinates) for city, coordinates in CITIES.items()]
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} city snapshots to {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
