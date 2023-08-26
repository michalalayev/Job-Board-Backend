from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    wish_list = "Wish List"
    applied = "Applied"
    interview = "Interview"
    offer = "Offer"
    terminated = "Terminated"


class JobEntity(BaseModel):
    id: int
    position: str
    company: str
    location: str | None = None
    status: Status = Status.wish_list
    created_date: datetime
    last_modified: datetime
    # actions: str = ":"
    # link: str
    # source: str
    # company_site: str

