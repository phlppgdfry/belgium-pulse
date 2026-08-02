# Belgium Pulse

Een interactieve Power BI-cockpit die toont hoe Belgische steden "ademen": weer, luchtkwaliteit en een samengestelde **chaos score** per stad. De basis is ontworpen om later spoor-, verkeer-, energie- en eventdata toe te voegen.

## Wat zit erin?

- Live, API-vrije weer- en luchtkwaliteitsophaling voor Brussel, Antwerpen, Gent, Luik en Charleroi.
- Een uitlegbare chaos score van 0–100, met goed afgebakende gewichten.
- Een verzorgd Power BI-startpakket: kleurenpalet, Power Query, DAX-measures en paginaplan.
- Demo-data zodat je meteen kunt ontwerpen zonder API-call.
- Een veilige basis voor publicatie naar Microsoft Fabric met `fabric-cicd`.

## Snel starten

```bash
cd belgium-pulse
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 scripts/fetch_open_data.py
```

De tweede opdracht schrijft het laatste stadsbeeld naar `data/processed/city_hourly.csv`. De publieke Open-Meteo-endpoints hebben geen sleutel nodig.

Open daarna [powerbi/README.md](powerbi/README.md) voor de Power BI Desktop-stappen.

## Dashboardverhaal

| Pagina | Vraag die ze beantwoordt | Hoofdvisuals |
| --- | --- | --- |
| Pulse now | Welke stad is nú het meest onder druk? | KPI's, scorekaart, ranglijst |
| City anatomy | Waardoor wordt de score veroorzaakt? | Decompositie, radar, detailkaart |
| Weather meets air | Is het comfortabel én gezond? | Scatterplot, temperatuurband, AQI-kaart |
| What if? | Wat doet een hittegolf of slechte lucht? | What-if parameters, scenario cards |
| Data lab | Kunnen we de bron vertrouwen? | Tijdstip, bronstatus, ruwe waarden |

## Projectstructuur

```text
belgium-pulse/
├── data/                 # demo-data, verwerkte live-data en gitignored ruwe responsen
├── docs/                 # metric- en databronbeschrijving
├── powerbi/              # Power Query, DAX, thema en rapportplan
├── scripts/              # ophalen en publiceren
├── src/belgium_pulse/    # scorelogica die ook getest wordt
├── tests/
└── .github/workflows/    # validatie en optionele Fabric-deploy
```

## Git-werkwijze

Gebruik `main` als stabiele versie en maak feature branches voor nieuwe datadomeinen, bijvoorbeeld `feature/irail-disruptions` of `feature/energy-prices`. Commit nooit tokens, lokale Power BI-cachebestanden of broncredentials.

## Fabric-deploy

Een deploy gebeurt pas wanneer je zelf een PBIP-project hebt opgeslagen in `powerbi/pbip/`. Zie [scripts/deploy_to_fabric.py](scripts/deploy_to_fabric.py) en de handmatige GitHub-workflow. De repository voert dus nooit ongevraagd een deploy uit.

## Roadmap

- [ ] iRail-verstoring als transit-druk
- [ ] Energieprijscomponent via een gelicentieerde bron
- [ ] TomTom/regionale verkeersdruk met eigen API-sleutel
- [ ] Historische opslag in Fabric Lakehouse
- [ ] Dagelijkse "Pulse Recap" naar Teams
