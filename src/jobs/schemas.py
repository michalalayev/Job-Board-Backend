# pydantic models

from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    wish_list = "Wish List"
    applied = "Applied"
    interview = "Interview"
    offer = "Offer"
    terminated = "Terminated"


class JobInputModel(BaseModel):
    position: str
    company: str
    location: str | None
    status: Status | None = Status.wish_list
    # link: str
    # source: str
    # company_site: str


class JobModel(JobInputModel):
    id: int
    # status: Status
    created_date: datetime
    last_modified: datetime
    actions: str = ":"
    # link: str
    # source: str
    # company_site: str


class JobUpdateModel(BaseModel):
    position: str | None
    company: str | None
    location: str | None
    status: str | None
    # link: str
    # source: str
    # company_site: str