from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class Status(str, Enum):
    wish_list = "Wish List"
    applied = "Applied"
    interview = "Interview"
    offer = "Offer"
    terminated = "Terminated"


class JobModel(BaseModel):
    id: int
    position: str
    company: str
    location: Optional[str]
    status: Status
    created_date: datetime
    last_modified: datetime
    actions: str = ":"
    # link: str
    # source: str
    # company_site: str


class JobInputModel(BaseModel):
    position: str
    company: str
    location: Optional[str]
    status: Optional[Status] = Status.wish_list
    # link: str
    # source: str
    # company_site: str


class JobUpdateModel(BaseModel):
    position: Optional[str]
    company: Optional[str]
    location: Optional[str]
    status: Optional[str]
    # link: str
    # source: str
    # company_site: str
