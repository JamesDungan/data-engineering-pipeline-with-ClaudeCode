# data-engineering-pipeline-with-ClaudeCode
Here we create an end-to-end data engineering pipeline using Calude Code via the VSCode extension

## Build the Data Engineering Project

This project is intentionally scoped as a Minimum Viable Product (MVP). The goal is not to build a production-grade data platform, but to create a complete, end-to-end data engineering slice that demonstrates how real analytics systems are structured.

In this MVP, we build a simple but credible analytics pipeline that:

1. **Ingests a CSV file** containing event data
2. **Loads the data into DuckDB** as a raw warehouse table (raw_events)
3. **Applies SQL-based transformations** to produce a clean, analytics-ready fact table (fct_events)
4. **Computes three core metrics** using DuckDB SQL
5. **Displays those metrics in a local Streamlit dashboard**

The full flow looks like this:

```
CSV file
  ↓
raw_events        (raw ingestion, 1:1 with source)
  ↓
fct_events        (typed, deduplicated, transformed)
  ↓
metrics           (daily count, 7-day rolling avg, top category)
  ↓
Streamlit UI      (local dashboard)
```

## Stack

- Python 3.11
- [uv](https://docs.astral.sh/uv/) for dependency and environment management
- [DuckDB](https://duckdb.org/) as the local database
- [Streamlit](https://streamlit.io/) for the dashboard
- [Pydantic](https://docs.pydantic.dev/) for data models
- [pytest](https://docs.pytest.org/) for tests

## Project structure

```
backend/
  db.py         # DuckDB connection + schema helpers
  ingest.py      # CSV -> raw_events ingestion command
  pipeline.py    # transform / metrics (not yet implemented)
  models.py      # Pydantic models
  sql/
    create_raw_events.sql
app/
  app.py         # Streamlit dashboard (not yet implemented)
data/
  sample.csv     # ~50-row sample dataset
tests/
  test_ingest.py
```

## Local setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you don't already have it:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. From the repo root, sync the environment (this also downloads Python 3.11 if needed):
   ```bash
   uv sync
   ```

## Run the ingest pipeline

Load `data/sample.csv` into a local DuckDB file (`data/warehouse.duckdb`) and print the row count:

```bash
uv run python -m backend.ingest
```

Expected output:

```
Ingested 50 rows into raw_events (data/warehouse.duckdb)
```

You can also point it at a different CSV or DuckDB file:

```bash
uv run python -m backend.ingest path/to/other.csv --db-path path/to/other.duckdb
```

## Run tests

```bash
uv run pytest
```

## Status

Scaffolding only: CSV ingestion into a `raw_events` table is implemented. Transform/metrics (`backend/pipeline.py`) and the Streamlit dashboard (`app/app.py`) are stubs to be built in later steps.

