from pydantic import BaseModel, EmailStr
from typing import List

# from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactModel(BaseModel):
    id: int
    name: str
    position: str
    company: str
    email: EmailStr | None
    phone_number: int | None
    linkedin: str | None
    website: str | None
    facebook: str | None
    github: str | None
    linked_jobs: List[int]  # or List[JobModel]
