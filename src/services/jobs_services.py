# from ..service import IService
from abc import ABC, abstractmethod

from typing import List

# from schemas.job_schemas import JobCreationAPIModel, JobUpdateAPIModel
from domain.job_entity import JobEntity
from repositories.jobs_repository import IJobsRepository, JobsRepository


class IJobsService(ABC):
    @abstractmethod
    def get_all_jobs(self) -> List[JobEntity]:
        pass

    @abstractmethod
    def get_job_by_id(self, job_id: int) -> JobEntity | None:
        pass

    @abstractmethod
    def create_job(self) -> JobEntity:
        pass

    # @abstractmethod
    # def delete_job(self, job_id: int) -> None:
    #     pass

    # @abstractmethod
    # def update_job(self, job_id: int) -> JobEntity:
    #     pass

    @abstractmethod
    def load_data_at_startup(self) -> None:
        pass


class JobsService(IJobsService):
    def __init__(self, jobs_repository: IJobsRepository | None = None) -> None:
        self.__jobs_repository = jobs_repository or JobsRepository()

    def get_all_jobs(self) -> List[JobEntity]:
        return self.__jobs_repository.get_all_jobs()

    def get_job_by_id(self, job_id: int) -> JobEntity | None:
        return self.__jobs_repository.get_job_by_id(job_id)

    def create_job(self) -> JobEntity:
        creation_time = datetime.now()
        global db_last
        id = db_last + 1
        db_last = id
        fields = {
            "id": id,
            "created_date": creation_time,
            "last_modified": creation_time,
        }
        new_job = JobEntity(**fields, **job_input.dict())
        db[id] = new_job
        return new_job

    def load_data_at_startup(self) -> None:
        self.__jobs_repository.load_data_to_table()
