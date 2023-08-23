from abc import ABC, abstractmethod
from typing import List
from models.job_models import JobSQLModel
from sqlmodel import Session, select
from database import engine
from db_items import db_sqlmodel

# from schemas.job_schemas import JobEntityModel, JobCreationModel, JobUpdateModel


class IJobsRepository(ABC):
    @abstractmethod
    def get_all_jobs(self) -> List[JobSQLModel]:
        pass

    @abstractmethod
    def get_job_by_id(self, job_id: int) -> JobSQLModel:
        pass

    @abstractmethod
    def create_job(self) -> JobSQLModel:
        pass

    @abstractmethod
    def delete_job(self, job_id: int) -> None:
        pass

    @abstractmethod
    def update_job(self, job_id: int) -> JobSQLModel:
        pass

    # @abstractmethod
    # def get_jobs_by_contact(self) -> List[JobSQLModel]:
    #     pass

    @abstractmethod
    def load_data_to_table(self):
        pass


class JobsRepository(IJobsRepository):
    def get_all_jobs(self) -> List[JobSQLModel]:
        return list(db_sqlmodel.values())

    def get_job_by_id(self, job_id: int) -> JobSQLModel:
        return db_sqlmodel[0]

    def create_job(self) -> JobSQLModel:
        return db_sqlmodel[0]

    def delete_job(self, job_id: int) -> None:
        pass

    def update_job(self, job_id: int) -> JobSQLModel:
        return db_sqlmodel[0]

    def load_data_to_table(self):
        with Session(engine) as session:
            # check if the table is already populated with data
            statement = select(JobSQLModel)
            results = session.exec(statement).first()

            # load data if there are no results
            if results is None:
                for job in db_sqlmodel.values():
                    session.add(job)
                session.commit()
