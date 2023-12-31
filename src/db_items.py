from typing import List, Dict
from domain.job_entity import JobEntity, Status
from datetime import datetime
from models.job_models import JobSQLModel

# global db_last
db_last: int = 10

db_entities: Dict[int, JobEntity] = {
    0: JobEntity(
        id=0,
        position="Backend Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2022, 11, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 11, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    1: JobEntity(
        id=1,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2021, 10, 24, 10, 33, 30, 0),
        last_modified=datetime(2021, 10, 30, 10, 33, 30, 0),
        status=Status.offer,
    ),
    2: JobEntity(
        id=2,
        position="Software Engineer",
        company="Taboola",
        location="Tel-Aviv",
        created_date=datetime(2019, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2019, 10, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    3: JobEntity(
        id=3,
        position="Backend Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2022, 8, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    4: JobEntity(
        id=4,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 33, 30, 0),
        status=Status.wish_list,
    ),
    5: JobEntity(
        id=5,
        position="Software Engineer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    6: JobEntity(
        id=6,
        position="Fullstack Engineer",
        company="Elbit",
        location="Holon",
        created_date=datetime(2023, 3, 24, 8, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 13, 33, 30, 0),
        status=Status.wish_list,
    ),
    7: JobEntity(
        id=7,
        position="Software Engineer",
        company="IronSource",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 10, 30, 10, 33, 30, 0),
        status=Status.terminated,
    ),
    8: JobEntity(
        id=8,
        position="Fullstack Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2019, 8, 24, 10, 33, 31, 0),
        last_modified=datetime(2019, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    9: JobEntity(
        id=9,
        position="Software Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 34, 30, 0),
        status=Status.wish_list,
    ),
    10: JobEntity(
        id=10,
        position="Sofware Developer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 29, 20, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 21, 44, 30, 0),
        status=Status.interview,
    ),
}


db_as_list: List[JobEntity] = [
    JobEntity(
        id=0,
        position="Backend Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2022, 11, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 11, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    JobEntity(
        id=1,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2021, 10, 24, 10, 33, 30, 0),
        last_modified=datetime(2021, 10, 30, 10, 33, 30, 0),
        status=Status.offer,
    ),
    JobEntity(
        id=2,
        position="Software Engineer",
        company="Taboola",
        location="Tel-Aviv",
        created_date=datetime(2019, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2019, 10, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    JobEntity(
        id=3,
        position="Backend Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2022, 8, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    JobEntity(
        id=4,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 33, 30, 0),
        status=Status.wish_list,
    ),
    JobEntity(
        id=5,
        position="Software Engineer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    JobEntity(
        id=6,
        position="Fullstack Engineer",
        company="Elbit",
        location="Holon",
        created_date=datetime(2023, 3, 24, 8, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 13, 33, 30, 0),
        status=Status.wish_list,
    ),
    JobEntity(
        id=7,
        position="Software Engineer",
        company="IronSource",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 10, 30, 10, 33, 30, 0),
        status=Status.terminated,
    ),
    JobEntity(
        id=8,
        position="Fullstack Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2019, 8, 24, 10, 33, 31, 0),
        last_modified=datetime(2019, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    JobEntity(
        id=9,
        position="Software Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 34, 30, 0),
        status=Status.wish_list,
    ),
    JobEntity(
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


db_sqlmodel: Dict[int, JobSQLModel] = {
    0: JobSQLModel(
        # id=0,
        position="Backend Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2022, 11, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 11, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    1: JobSQLModel(
        # id=1,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2021, 10, 24, 10, 33, 30, 0),
        last_modified=datetime(2021, 10, 30, 10, 33, 30, 0),
        status=Status.offer,
    ),
    2: JobSQLModel(
        # id=2,
        position="Software Engineer",
        company="Taboola",
        location="Tel-Aviv",
        created_date=datetime(2019, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2019, 10, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    3: JobSQLModel(
        # id=3,
        position="Backend Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2022, 8, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    4: JobSQLModel(
        # id=4,
        position="Fullstack Engineer",
        company="Google",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 33, 30, 0),
        status=Status.wish_list,
    ),
    5: JobSQLModel(
        # id=5,
        position="Software Engineer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 9, 30, 10, 33, 30, 0),
        status=Status.interview,
    ),
    6: JobSQLModel(
        # id=6,
        position="Fullstack Engineer",
        company="Elbit",
        location="Holon",
        created_date=datetime(2023, 3, 24, 8, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 13, 33, 30, 0),
        status=Status.wish_list,
    ),
    7: JobSQLModel(
        # id=7,
        position="Software Engineer",
        company="IronSource",
        location="Tel-Aviv",
        created_date=datetime(2022, 6, 24, 10, 33, 30, 0),
        last_modified=datetime(2022, 10, 30, 10, 33, 30, 0),
        status=Status.terminated,
    ),
    8: JobSQLModel(
        # id=8,
        position="Fullstack Engineer",
        company="Wix",
        location="Herzliya",
        created_date=datetime(2019, 8, 24, 10, 33, 31, 0),
        last_modified=datetime(2019, 9, 25, 10, 33, 30, 0),
        status=Status.applied,
    ),
    9: JobSQLModel(
        # id=9,
        position="Software Engineer",
        company="Verily",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 24, 10, 33, 30, 0),
        last_modified=datetime(2023, 3, 24, 10, 34, 30, 0),
        status=Status.wish_list,
    ),
    10: JobSQLModel(
        # id=10,
        position="Sofware Developer",
        company="Check Point",
        location="Tel-Aviv",
        created_date=datetime(2023, 3, 29, 20, 33, 30, 0),
        last_modified=datetime(2023, 3, 29, 21, 44, 30, 0),
        status=Status.interview,
    ),
}
