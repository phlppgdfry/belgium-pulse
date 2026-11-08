# Optional live-data and Power BI starter

The runnable browser demo uses synthetic fixtures. The existing `scripts/fetch_open_data.py` is a separate Open-Meteo CSV ingestion example; it is not called automatically by the demo. Install its existing Python project dependencies with `python3 -m pip install -e .` if you want to explore it. Its output is `data/processed/city_hourly.csv`.

`powerbi/` contains Power Query, DAX, a theme and a report plan. No finished PBIX/PBIP report or Fabric deployment is claimed. `scripts/deploy_to_fabric.py` and the manual workflow remain optional scaffolding that require your own workspace and project. None of this is needed for `python3 -m demo.server`.

Existing local CSV edits were preserved during the portfolio upgrade; they were not included in the new demo baseline or committed as fresh live observations.
