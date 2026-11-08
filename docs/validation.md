# Validation evidence

Validation date: 8 November 2026. Fixtures represent June 2026 and are intentionally frozen. No historical business outcomes are inferred from this validation.

## Recorded local result

Python 3.14.10: **18 tests passed**. Chromium: **6 tests passed**. JavaScript syntax checks and Python compilation passed. The report command reproduced the committed synthetic baseline.

## Automated checks

- `make check`: Python unit/integration tests, HTTP round trips, invalid input, read/export round trip, durable state, stale-write rejection, simultaneous updates and audit-failure rollback; Python compilation; JavaScript syntax checks.
- `npm run test:e2e`: six Chromium tests covering served brand assets, filters/empty state, responsive layouts at 390/768/1440 px and the domain workflow with reload persistence.
- `make report`: baseline JSON and CSV generated from the same domain calculations used by the browser.

Domain coverage: Weighted contributions, rounding, extreme inputs, non-finite validation, restore, HTTP writes and full browser persistence.

## Browser review

The native browser entry point reported no browser available, so review used the shared Playwright browser. The core flow was exercised through real forms and buttons against the local Python server. Reload persistence, visible success and rejection messages, record selection and mobile document width were checked. Screenshots are actual rendered pages, not design mockups.

1. Select Charleroi and inspect the four weighted score contributions.
2. Set the apparent temperature to 35 °C and apply the scenario. Watch the score, ranking and mean change.
3. Reload to verify persistence, then restore the original inputs. Export the current observations as CSV.

See [desktop screenshot](preview.png), [mobile screenshot](mobile.png), and the current [GitHub Actions run](https://github.com/phlppgdfry/belgium-pulse/actions/workflows/demo.yml). The badge reports the remote result; this document describes the checks, not an invented production certification.

## Limits of the evidence

The suite tests a local single-workspace product with synthetic records. It does not establish external integration reliability, real user outcomes, scale, production security, legal compliance or clinical validity. No live traffic, iRail, energy feed, historical lakehouse, production Power BI report or Fabric deployment is delivered by this demo. The existing Power BI assets are a starter kit. The city index has no scientific validation.
