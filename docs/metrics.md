# Chaos score

De chaos score is een verklaarbare indicatie, geen officiële risico-index. Elke component wordt genormaliseerd naar 0–100 en gewogen opgeteld.

| Component | Gewicht | Intuïtie |
| --- | ---: | --- |
| Europese luchtkwaliteitsindex | 45% | Slechte lucht heeft de grootste impact op dagelijks comfort. |
| Hittestress / koude | 20% | Afwijking van een aangename 18°C. |
| Neerslagkans | 15% | Meer kans op regen betekent meer frictie onderweg. |
| Wind | 20% | Wind beïnvloedt fietsers, openbaar vervoer en buitenactiviteiten. |

Formule:

```text
score = 0.45 × AQI + 0.20 × temperatuurstress + 0.15 × neerslag + 0.20 × wind
```

De score wordt altijd begrensd op 0–100. Later kan deze worden uitgebreid met transit-, verkeer-, energie- en eventdruk. Houd die dimensies apart in de semantic model-tabel, zodat de score transparant blijft.

