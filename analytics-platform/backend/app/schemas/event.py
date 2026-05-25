from pydantic import BaseModel
from typing import Dict, Any


class EventCreate(BaseModel):

    event_type: str

    payload: Dict[str, Any]