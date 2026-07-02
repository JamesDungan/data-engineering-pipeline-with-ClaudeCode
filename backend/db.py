from pathlib import Path

import duckdb

# DuckDB is embedded (like SQLite) - this file path IS the database, no server needed.
DEFAULT_DB_PATH = Path("data/warehouse.duckdb")
SQL_DIR = Path(__file__).parent / "sql"


def get_connection(db_path: Path = DEFAULT_DB_PATH) -> duckdb.DuckDBPyConnection:
    # Make sure data/ exists before DuckDB tries to create the .duckdb file in it.
    db_path.parent.mkdir(parents=True, exist_ok=True)
    # connect() creates the file on first call, or opens it if it already exists.
    return duckdb.connect(str(db_path))


def run_schema(con: duckdb.DuckDBPyConnection, schema_file: str = "create_raw_events.sql") -> None:
    # Schema lives in a .sql file (backend/sql/) rather than inline Python strings,
    # so it reads like normal SQL and is easy to extend as more tables are added.
    sql = (SQL_DIR / schema_file).read_text()
    con.execute(sql)
