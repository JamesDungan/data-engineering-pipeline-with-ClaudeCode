from datetime import datetime

from pydantic import BaseModel


# Mirrors the raw_events table schema (backend/sql/create_raw_events.sql) so
# individual rows can be validated/typed in Python, e.g. before or after a DuckDB query.
class RawEvent(BaseModel):
    event_time: datetime
    user_id: int
    event_name: str
    category: str
    amount: float
