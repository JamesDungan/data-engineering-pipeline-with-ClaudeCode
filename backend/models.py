from datetime import datetime

from pydantic import BaseModel


class RawEvent(BaseModel):
    event_time: datetime
    user_id: int
    event_name: str
    category: str
    amount: float
