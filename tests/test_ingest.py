from pathlib import Path

from backend.ingest import DEFAULT_CSV_PATH, ingest_csv


def test_ingest_csv_row_count(tmp_path: Path) -> None:
    db_path = tmp_path / "test.duckdb"

    row_count = ingest_csv(DEFAULT_CSV_PATH, db_path)

    expected = sum(1 for _ in DEFAULT_CSV_PATH.open()) - 1  # exclude header
    assert row_count == expected
