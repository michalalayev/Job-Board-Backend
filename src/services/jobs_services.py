# from ..service import IService
from abc import ABC, abstractmethod
# from typing import List
# from schemas.job_schemas import JobEntityModel, JobCreationModel, JobUpdateModel
from repositories.jobs_repository import IJobsRepository, JobsRepository


class IJobsService(ABC):
    # @abstractmethod
    # def get_all_jobs(self) -> List[JobEntityModel]:
    #     pass

    # @abstractmethod
    # def get_job_by_id(self, job_id: int) -> JobEntityModel:
    #     pass

    # @abstractmethod
    # def create_job(self) -> JobEntityModel:
    #     pass

    # @abstractmethod
    # def delete_job(self, job_id: int) -> None:
    #     pass

    # @abstractmethod
    # def update_job(self, job_id: int) -> JobEntityModel:
    #     pass

    @abstractmethod
    def load_data_at_startup(self) -> None:
        pass


class JobsService(IJobsService):
    def __init__(self, jobs_repository: IJobsRepository | None = None) -> None:
        self.__jobs_repository = (
            jobs_repository if jobs_repository is not None else JobsRepository()
        )

    def load_data_at_startup(self) -> None:
        self.__jobs_repository.load_data_to_table()
