# Report plan — Belgium Pulse

## 1. Pulse now

**Doel:** in vijf seconden begrijpen wat er speelt.

- Bovenrij: `Average Chaos Score`, `Pulse Status`, `Highest Pressure City`, `Data Freshness UTC`.
- Midden: Azure Maps met stadslocaties; bubbelgrootte = chaos score, kleur = Europese AQI.
- Rechts: horizontale ranglijst stad × chaos score, met voorwaardelijke kleur.
- Onder: compacte matrix met temperatuur, wind, regen en AQI.

## 2. City anatomy

**Doel:** de oorzaak achter de score zichtbaar maken.

- Stadsslicer linksboven.
- Decomposition tree: chaos score → Europese AQI → wind → regen → temperatuurstress.
- Radar- of kolomgrafiek met de vier dimensies.
- Tekstkaart met een dynamische conclusie, bijvoorbeeld: “Antwerpen wordt vooral gedreven door luchtkwaliteit.”

## 3. Weather meets air

**Doel:** comfort en gezondheid naast elkaar zetten.

- Scatter: temperatuur (x), PM2.5 (y), bubbel = wind, kleur = stad.
- Combo chart: temperatuur en neerslagkans per stad.
- Referentielijnen: 18°C comfortpunt en AQI 40 als aandachtspunt.

## 4. What if?

**Doel:** de score speels en uitlegbaar maken.

- Maak twee What-if parameters: `Heat scenario` (-5 tot 15) en `Rain scenario` (0 tot 100).
- Grote card: `Scenario Chaos Score`.
- Waterfall die basis, hitte-effect en regeffect toont.
- Hou de pagina duidelijk gelabeld als simulatie, niet als voorspelling.

## 5. Data lab

**Doel:** vertrouwen en onderhoud mogelijk maken.

- Tabel met alle bronvelden en tijdstip.
- Cards voor aantal steden en laatste refresh.
- Beschrijving van Open-Meteo, gebruikte formule en uitbreidingsroadmap.

## Designregels

- Gebruik donker nachtblauw als canvas, niet als "inktkleur" voor tekst.
- Accentgroen = rustig/gezond; amber = aandacht; koraal = druk.
- Maximaal drie grote visuals per pagina.
- Gebruik voldoende lege ruimte en laat KPI's leidend zijn.

