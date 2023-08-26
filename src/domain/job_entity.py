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
    actions: str = ":"
    # link: str
    # source: str
    # company_site: str


# if __name__ == '__main__':
#     j = JobEntity(
#         id=1,
#         position="Fullstack Engineer",
#         company="Google",
#         location="Tel-Aviv",
#         created_date=datetime(2021, 10, 24, 10, 33, 30, 0),
#         last_modified=datetime(2021, 10, 30, 10, 33, 30, 0),
#         status=Status.offer,
#     )
#     d = j.__dict__
#     print(d['last_modified'])
#     print(d['status'])
#     print(d['created_date'])
