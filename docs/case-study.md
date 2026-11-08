# Belgium Pulse — delivery case study

## Problem and intended user

City-level weather and air observations are hard to compare when each signal has a different unit and scale.

## Delivered vertical slice

An interactive Belgian city observatory with a transparent weighted pressure index and persistent what-if scenarios.

1. Select Charleroi and inspect the four weighted score contributions.
2. Set the apparent temperature to 35 °C and apply the scenario. Watch the score, ranking and mean change.
3. Reload to verify persistence, then restore the original inputs. Export the current observations as CSV.

## Acceptance criteria mapped to evidence

| Criterion | Verification |
| --- | --- |
| A reviewer can run the product without external credentials | `python3 -m demo.server`; standard-library runtime |
| Domain constraints are enforced on the server | `tests/test_demo_domain.py`; invalid transitions and boundary cases |
| Successful actions survive a new connection | `PersistenceTests.test_mutation_persists_and_is_audited` |
| A stale edit cannot overwrite newer state | Version conflict and simultaneous update tests |
| An audit write failure leaves the record unchanged | Fault-injected SQLite audit failure test |
| The main task works through the rendered interface | Domain workflow in `tests/browser/workspace.spec.cjs` |
| The interface works at mobile and desktop widths | 390, 768 and 1440 px browser tests; screenshots in `docs/` |
| Reported numbers can be reproduced | `python3 -m demo.report`; committed baseline JSON and CSV |

Domain-specific evidence: Weighted contributions, rounding, extreme inputs, non-finite validation, restore, HTTP writes and full browser persistence.

## What this demonstrates

Requirements are reduced to a coherent executable workflow, rather than a catalogue of disconnected features. Input contracts, state ownership, failure states, persistence and explanations are part of the product. Design choices and operational limits are recorded so another engineer can inspect the implementation and reproduce its behaviour.

## What it does not prove

No live traffic, iRail, energy feed, historical lakehouse, production Power BI report or Fabric deployment is delivered by this demo. The existing Power BI assets are a starter kit. The city index has no scientific validation.

No user study, commercial result, uptime, production scale, legal compliance or measured improvement is claimed. The historical concept is context, not evidence.
