from typing import List, Dict
from .schemas import JobModel, Status
from datetime import datetime

db: Dict[int, JobModel] = {
    0: JobModel(
        id=0,
        position="Backend Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2022, 11, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 11, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    1: JobModel(
        id=1,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2021, 10, 24, 10, 33, 30, 0),
        last_modified=datetime(2021, 10, 30, 10, 33, 30, 0),
        status=Status.offer,
    ),
    2: JobModel(
        id=2,
        position="Software Engineer",
        company="Taboola",
        location="Tel-Aviv",
        created_date=datetime(2019, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2019, 10, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    3: JobModel(
        id=3,
        position="Backend Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2022, 8, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    4: JobModel(
        id=4,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 33, 30, 0),
        status=Status.wish_list,
    ),
    5: JobModel(
        id=5,
        position="Software Engineer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    6: JobModel(
        id=6,
        position="Fullstack Engineer",
        company="Elbit",
        location="Holon",
        created_date=datetime(2023, 3, 24, 8, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 13, 33, 30, 0),
        status=Status.wish_list,
    ),
    7: JobModel(
        id=7,
        position="Software Engineer",
        company="IronSource",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 10, 30, 10, 33, 30, 0),
        status=Status.terminated,
    ),
    8: JobModel(
        id=8,
        position="Fullstack Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2019, 8, 24, 10, 33, 31, 0),
        last_modified=datetime(2019, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    9: JobModel(
        id=9,
        position="Software Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 34, 30, 0),
        status=Status.wish_list,
    ),
    10: JobModel(
        id=10,
        position="Sofware Developer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 29, 20, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 21, 44, 30, 0),
        status=Status.interview,
    ),
}


db_as_list: List[JobModel] = [
    JobModel(
        id=0,
        position="Backend Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2022, 11, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 11, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    JobModel(
        id=1,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2021, 10, 24, 10, 33, 30, 0),
        last_modified=datetime(2021, 10, 30, 10, 33, 30, 0),
        status=Status.offer,
    ),
    JobModel(
        id=2,
        position="Software Engineer",
        company="Taboola",
        location="Tel-Aviv",
        created_date=datetime(2019, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2019, 10, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    JobModel(
        id=3,
        position="Backend Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2022, 8, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    JobModel(
        id=4,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 33, 30, 0),
        status=Status.wish_list,
    ),
    JobModel(
        id=5,
        position="Software Engineer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    JobModel(
        id=6,
        position="Fullstack Engineer",
        company="Elbit",
        location="Holon",
        created_date=datetime(2023, 3, 24, 8, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 13, 33, 30, 0),
        status=Status.wish_list,
    ),
    JobModel(
        id=7,
        position="Software Engineer",
        company="IronSource",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 10, 30, 10, 33, 30, 0),
        status=Status.terminated,
    ),
    JobModel(
        id=8,
        position="Fullstack Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2019, 8, 24, 10, 33, 31, 0),
        last_modified=datetime(2019, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    JobModel(
        id=9,
        position="Software Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 34, 30, 0),
        status=Status.wish_list,
    ),
    JobModel(
        id=10,
        position="Sofware Developer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 29, 20, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 21, 44, 30, 0),
        status=Status.interview,
    ),
]

# vals = list(db.values())
# print(type(vals))
# print(type(vals[0]))
# d = vals[0].json()
# print(type(d))
# c = {"detail": "Invalid X-Token header"}
