export function inspect(r) {
  return {
    fields: [
      [
        "Observation",
        r.scenario
          ? "Local what-if scenario"
          : "Synthetic baseline, 15 June 2026",
      ],
      ...Object.entries(r.contributions).map(([k, v]) => [
        k,
        `${v.toFixed(2)} points`,
      ]),
      ["European AQI", r.aqi],
      ["Rain probability", `${r.rain}%`],
      ["Wind", `${r.wind} km/h`],
    ],
    forms: [
      {
        title: "What if?",
        help: "Change the inputs to see how the weighted pressure score responds.",
        action: "scenario",
        button: "Apply scenario",
        success:
          "Scenario saved. The score and its contributions have been recalculated.",
        fields: [
          {
            key: "temperature",
            label: "Apparent temperature · °C",
            type: "number",
            min: -40,
            max: 60,
            step: 0.1,
            value: r.temperature,
          },
          {
            key: "rain",
            label: "Rain probability · %",
            type: "number",
            min: 0,
            max: 100,
            step: 0.1,
            value: r.rain,
          },
          {
            key: "wind",
            label: "Wind speed · km/h",
            type: "number",
            min: 0,
            max: 200,
            step: 0.1,
            value: r.wind,
          },
          {
            key: "aqi",
            label: "European AQI",
            type: "number",
            min: 0,
            max: 500,
            step: 0.1,
            value: r.aqi,
          },
        ],
      },
      ...(r.scenario
        ? [
            {
              title: "Baseline",
              action: "restore",
              button: "Restore original inputs",
              fields: [],
            },
          ]
        : []),
    ],
    note: "Each signal is capped at 100 before weighting. AQI values above 100 therefore have the same contribution. Live ingestion and the demo are separate.",
  };
}
