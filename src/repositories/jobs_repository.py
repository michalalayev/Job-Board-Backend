from abc import ABC, abstractmethod
from typing import List
from models.job_models import JobSQLModel
from sqlmodel import Session, select
from database import engine
from db_items import db_entities, db_last, db_sqlmodel
from domain.job_entity import JobEntity
from datetime import datetime

# from schemas.job_schemas import JobEntityModel, JobCreationModel, JobUpdateModel


class IJobsRepository(ABC):
    @abstractmethod
    def get_all_jobs(self) -> List[JobEntity]:
        pass

    @abstractmethod
    def get_job_by_id(self, job_id: int) -> JobEntity | None:
        pass

    @abstractmethod
    def create_job(self, job_to_create: JobEntity) -> JobEntity:  # no client-assigned ids
        pass

    @abstractmethod
    def delete_job(self, job_id: int) -> bool:
        pass

    @abstractmethod
    def update_job(self, job_id: int, job_update: JobEntity) -> JobEntity | None:
        pass

    # @abstractmethod
    # def get_jobs_by_contact(self) -> List[JobEntity]:
    #     pass

    # @abstractmethod
    # @staticmethod
    # def convert_model_to_entity(job_sqlmodel: JobSQLModel) -> JobEntity:
    #     pass

    @abstractmethod
    def load_data_to_table(self) -> None:
        pass

    def delete_data_from_table(self) -> None:
        pass


class JobsRepository(IJobsRepository):
    def __init__(self) -> None:
        self.session = Session(engine)

    @staticmethod
    def __convert_model_to_entity(job_sqlmodel: JobSQLModel) -> JobEntity:
        job_data = job_sqlmodel.dict()
        return JobEntity(**job_data)

    @staticmethod
    def __convert_entity_to_model(job_entity: JobEntity) -> JobSQLModel:
        job_data = job_entity.dict(exclude={"id"})
        return JobSQLModel(**job_data)

    def get_all_jobs(self) -> List[JobEntity]:
        with self.session as session:
            statement = select(JobSQLModel)
            results = session.exec(statement)  # results is an iterable
            job_entities = [
                JobsRepository.__convert_model_to_entity(job) for job in results.all()
            ]  # all() returns a list of the objects
            return job_entities

    def get_job_by_id(self, job_id: int) -> JobEntity | None:
        with self.session as session:
            job = session.get(JobSQLModel, job_id)
            if job:
                job = JobsRepository.__convert_model_to_entity(job)
            return job

    def create_job(self, job_to_create: JobEntity) -> JobEntity:
        with self.session as session:
            job_sqlmodel = JobsRepository.__convert_entity_to_model(job_to_create)
            session.add(job_sqlmodel)
            session.commit()
            session.refresh(job_sqlmodel)
            created_job = JobsRepository.__convert_model_to_entity(job_sqlmodel)
            return created_job

    def delete_job(self, job_id: int) -> bool:
        with self.session as session:
            job = session.get(JobSQLModel, job_id)
            if job:
                session.delete(job)
                session.commit()
                return True
            return False

    def update_job(self, job_id: int, job_update: JobEntity) -> JobEntity | None:
        with self.session as session:
            stored_job = session.get(JobSQLModel, job_id)
            if stored_job:
                for key, value in job_update.dict(exclude={"id"}).items():
                    setattr(stored_job, key, value)
                # updated_job = stored_job.copy(update=job_update.dict(exclude={"id"})) - error
                session.add(stored_job)
                session.commit()
                session.refresh(stored_job)
                return JobsRepository.__convert_model_to_entity(stored_job)
            return None

    def load_data_to_table(self) -> None:
        with self.session as session:
            # check if the table is already populated with data
            statement = select(JobSQLModel)
            results = session.exec(statement).first()
            # results is an iterable, and then we take only its first element

            # load data if there are no results
            if results is None:
                for job in db_sqlmodel.values():
                    session.add(job)
                session.commit()

    def delete_data_from_table(self) -> None:  # deletes only the rows, table stays
        with self.session as session:
            statement = select(JobSQLModel)
            results = session.exec(statement)
            if results:
                for job in results:
                    session.delete(job)
                session.commit()


"""
with block causes the session to close automatically at the end of the block.
I've created the field session to hold a single session but allow perform different 
methods all in one session.
I wonder if the with block prevents this - check later.
"""


class JobsInMemoryList(IJobsRepository):
    def __init__(self) -> None:
        self.db = db_entities

    def get_all_jobs(self) -> List[JobEntity]:
        return list(self.db.values())

    def get_job_by_id(self, job_id: int) -> JobEntity | None:
        if job_id in self.db:
            return self.db[job_id]
        return None

    def create_job(self, job_to_create: JobEntity) -> JobEntity:
        creation_time = datetime.now()
        global db_last
        id = db_last + 1
        db_last = id
        fields = {
            "id": id,
            "created_date": creation_time,
            "last_modified": creation_time,
        }
        new_job = JobEntity(**fields, **job_to_create.dict())
        self.db[id] = new_job
        return new_job

    def delete_job(self, job_id: int) -> bool:
        if job_id in self.db:
            self.db.pop(job_id)
            return True
        return False

    def update_job(self, job_id: int, job_update: JobEntity) -> JobEntity | None:
        if job_id in self.db:
            stored_job = self.db[job_id]
            update_data = job_update.dict(exclude_unset=True)
            # don't include in the dict the model fields that had no value in job_update object
            # if exclude_unset=False then fields that weren't passed in job_update will be None
            print(
                "update_data dict without exclude_unset: \n",
                job_update.dict(exclude_unset=False),
            )
            print("update data dict: \n", update_data)
            update_data["last_modified"] = datetime.now()
            updated_job = stored_job.copy(update=update_data)
            print("updated_job:\n", updated_job)
            self.db[job_id] = updated_job
            print("db[job_id]:\n", self.db[job_id])
            return updated_job
        return None

    def load_data_to_table(self) -> None:
        return

    def delete_data_from_table(self) -> None:
        return
