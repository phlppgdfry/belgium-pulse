from demo.contracts import number, record, metric


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from belgium_pulse.scoring import chaos_score, temperature_stress, clamp  # noqa: E402


CONFIG = {
    "columns": [
        ["name", "City"],
        ["status", "Pressure"],
        ["value", "Score / 100"],
        ["context", "Feels like"],
    ],
    "title": "Belgium Pulse",
    "heading": "A clearer view of city pressure.",
    "subtitle": "Compare weather and air quality across five Belgian cities. Inspect every contribution, then test your own scenario.",
    "section": "City observatory",
    "list_title": "City comparison",
    "theme": "pulse",
    "port": 8111,
    "clock": "Fixture snapshot · 15 June 2026, 08:00 UTC",
}


ACTIONS = frozenset(["scenario", "restore"])


def seed():
    values = [
        ("brussels", "Brussel", 23, 35, 14, 38),
        ("antwerp", "Antwerpen", 25, 20, 18, 57),
        ("ghent", "Gent", 21, 45, 12, 29),
        ("liege", "Luik", 27, 15, 9, 43),
        ("charleroi", "Charleroi", 24, 40, 16, 64),
    ]
    return [
        dict(id=i, name=n, temperature=t, rain=r, wind=w, aqi=a, scenario=False)
        for i, n, t, r, w, a in values
    ]


def contributions(r):
    return {
        "Air quality (45%)": round(0.45 * clamp(r["aqi"]), 2),
        "Temperature (20%)": round(0.20 * temperature_stress(r["temperature"]), 2),
        "Rain probability (15%)": round(0.15 * clamp(r["rain"]), 2),
        "Wind (20%)": round(0.20 * clamp(r["wind"] * 2), 2),
    }


def score(r):
    return chaos_score(
        apparent_temperature_c=r["temperature"],
        precipitation_probability_pct=r["rain"],
        wind_speed_kmh=r["wind"],
        european_aqi=r["aqi"],
    )


def present(records):
    return [
        r
        | {
            "status": "High" if score(r) >= 60 else "Moderate" if score(r) >= 30 else "Low",
            "value": score(r),
            "context": f"{r['temperature']:g} °C",
            "contributions": contributions(r),
        }
        for r in sorted(records, key=score, reverse=True)
    ]


def metrics(records):
    scores = [score(r) for r in records]
    return [
        metric("Cities observed", len(records), "Five independent fixture observations"),
        metric("Mean pressure", f"{sum(scores) / len(scores):.1f}", "Equal weight per city"),
        metric(
            "Highest pressure", max(records, key=score)["name"], "Inspect the weighted contribution"
        ),
        metric(
            "Active scenarios",
            sum(r["scenario"] for r in records),
            "Editable locally; source data preserved",
        ),
    ]


def analysis(records):
    return {
        "title": "Pressure, explained.",
        "headline": "Four signals. One transparent score.",
        "description": "A portfolio index for comparison, not a health or mobility advisory. Air quality weighs 45%, temperature 20%, rain 15%, wind 20%.",
        "bars_title": "Pressure by city · 0–100",
        "bars": [
            {"label": r["name"], "value": score(r), "display": str(score(r))}
            for r in sorted(records, key=score, reverse=True)
        ],
    }


def execute(records, p):
    r = record(records, p)
    if p["action"] == "scenario":
        r.update(
            temperature=number(p, "temperature", -40, 60),
            rain=number(p, "rain", 0, 100),
            wind=number(p, "wind", 0, 200),
            aqi=number(p, "aqi", 0, 500),
            scenario=True,
        )
    elif p["action"] == "restore":
        r = next(s for s in seed() if s["id"] == r["id"])
    else:
        raise ValueError("Unknown action")
    return r
