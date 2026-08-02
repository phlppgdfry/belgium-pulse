# Power BI build guide

Deze repository bewaart alles wat handmatig en betrouwbaar in Git kan: de data, query, measures, thema en visual-specificatie. Laat **Power BI Desktop** zelf het PBIP-bestand genereren; de reportmetadata is tijdens de PBIP-preview nog gevoelig voor handmatig bewerken.

## 1. Maak het PBIP-project

1. Open Power BI Desktop op Windows.
2. Activeer **File → Options and settings → Options → Preview features → Power BI Project (.pbip) save option**.
3. Kies **File → Save As → Power BI Project** en sla op in `powerbi/pbip/` met naam `BelgiumPulse`.
4. Commit daarna de aangemaakte `.pbip`, `.Report` en `.SemanticModel` mappen. Lokale cachebestanden worden al genegeerd.

## 2. Laad de data

1. Voer in de repository-root `python3 scripts/fetch_open_data.py` uit.
2. In Power BI Desktop: **Transform data → Manage parameters → New parameter**.
3. Noem het tekstparameter `DataRoot` en geef de absolute map op, bijvoorbeeld `C:/Users/you/belgium-pulse/data/processed`.
4. Maak een **Blank query**, open Advanced Editor en plak [power-query/CitySnapshot.pq](power-query/CitySnapshot.pq).
5. Hernoem de query naar `City Snapshot`, controleer de kolomtypes en laad de tabel.

## 3. Model en DAX

- Markeer `observed_at_utc` als datum/tijd en `city` als tekst/categorie City.
- Selecteer `latitude` en `longitude` als Latitude/Longitude data category.
- Maak de measures in [dax/Measures.dax](dax/Measures.dax) aan onder `City Snapshot`.
- Importeer [theme/belgium-pulse-theme.json](theme/belgium-pulse-theme.json) via **View → Themes → Browse for themes**.

## 4. Bouw de pagina's

Volg [report-plan.md](report-plan.md). Begin met de eerste pagina; die geeft meteen een bruikbare, rustige cockpit zonder custom visuals.

## 5. Publiceren

Publiceer eerst handmatig naar je Fabric workspace. Zodra `powerbi/pbip/` in Git staat, kun je `fabric-cicd` gebruiken:

```bash
~/.local/share/fabric-cicd/bin/python scripts/deploy_to_fabric.py \
  --workspace-name "Belgium Pulse Dev" \
  --environment dev
```

De eerste keer moeten de credentials voor databronnen nog in de Fabric-portal worden ingesteld.

