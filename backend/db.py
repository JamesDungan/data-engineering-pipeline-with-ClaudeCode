from pathlib import Path

import duckdb

DEFAULT_DB_PATH = Path("data/warehouse.duckdb")
SQL_DIR = Path(__file__).parent / "sql"


def get_connection(db_path: Path = DEFAULT_DB_PATH) -> duckdb.DuckDBPyConnection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))


def run_schema(con: duckdb.DuckDBPyConnection, schema_file: str = "create_raw_events.sql") -> None:
    sql = (SQL_DIR / schema_file).read_text()
    con.execute(sql)
