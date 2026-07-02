import argparse
from pathlib import Path

from backend.db import DEFAULT_DB_PATH, get_connection, run_schema

DEFAULT_CSV_PATH = Path("data/sample.csv")


def ingest_csv(csv_path: Path = DEFAULT_CSV_PATH, db_path: Path = DEFAULT_DB_PATH) -> int:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    con = get_connection(db_path)
    run_schema(con)
    con.execute("DELETE FROM raw_events")
    con.execute(
        f"INSERT INTO raw_events SELECT * FROM read_csv('{csv_path.as_posix()}', header=true)"
    )
    row_count = con.execute("SELECT COUNT(*) FROM raw_events").fetchone()[0]
    con.close()
    return row_count


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a CSV file into the raw_events table")
    parser.add_argument("csv_path", nargs="?", default=str(DEFAULT_CSV_PATH))
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    args = parser.parse_args()

    row_count = ingest_csv(Path(args.csv_path), Path(args.db_path))
    print(f"Ingested {row_count} rows into raw_events ({args.db_path})")


if __name__ == "__main__":
    main()
