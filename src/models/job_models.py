# db models (using SQLModel)

from sqlmodel import Field, SQLModel
from datetime import datetime
from schemas.job_schemas import Status


class JobSQLModel(SQLModel, table=True):
    __tablename__ = "jobs"
    id: int | None = Field(default=None, primary_key=True)
    position: str
    company: str
    location: str | None = None
    status: Status  # = Status.wish_list
    created_date: datetime
    last_modified: datetime
    # link: str
    # source: str
    # company_site: str
