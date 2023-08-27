# pydantic models for the API

from pydantic import BaseModel
from domain.job_entity import Status


class JobCreationAPIModel(BaseModel):
    position: str
    company: str
    location: str | None = None
    status: Status | None = Status.wish_list
    # link: str
    # source: str
    # company_site: str


class JobUpdateAPIModel(BaseModel):
    position: str | None = None
    company: str | None = None
    location: str | None = None
    status: Status | None = None
    # link: str
    # source: str
    # company_site: str
