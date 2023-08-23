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


class JobCreationModel(BaseModel):
    position: str
    company: str
    location: str | None = None
    status: Status | None = Status.wish_list
    # link: str
    # source: str
    # company_site: str


class JobEntityModel(BaseModel):
    id: int
    position: str
    company: str
    location: str | None = None
    status: Status = Status.wish_list
    created_date: datetime
    last_modified: datetime
    actions: str = ":"
    # link: str
    # source: str
    # company_site: str


class JobUpdateModel(BaseModel):
    position: str | None = None
    company: str | None = None
    location: str | None = None
    status: str | None = None
    # link: str
    # source: str
    # company_site: str
