# test-repo-largefile

QA test repo for ABK-3826: code-graph line counting for large (>5 MiB) files.

Large files (all exceed the 5 MiB threshold):
- `data/events.csv` — ~14 MiB, 90k rows of event telemetry
- `data/product-catalog.xml` — ~5.8 MiB, 18k product entries
- `data/app.log` — ~6.1 MiB, 70k log lines

Source code:
- `src/ingest.py` — streaming ingest helpers
