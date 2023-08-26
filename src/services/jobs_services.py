# from ..service import IService
from abc import ABC, abstractmethod

from typing import List
from datetime import datetime

from schemas.job_schemas import JobCreationAPIModel, JobUpdateAPIModel
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
    def create_job(self, job_input: JobCreationAPIModel) -> JobEntity:
        pass

    @abstractmethod
    def delete_job(self, job_id: int) -> bool:
        pass

    @abstractmethod
    def update_job(self, job_id: int, job_update_model: JobUpdateAPIModel) -> JobEntity | None:
        pass

    @abstractmethod
    def load_data_at_startup(self) -> None:
        pass

    @abstractmethod
    def delete_data_from_table(self) -> None:
        pass


class JobsService(IJobsService):
    def __init__(self, jobs_repository: IJobsRepository | None = None) -> None:
        self.__jobs_repository = jobs_repository or JobsRepository()

    def get_all_jobs(self) -> List[JobEntity]:
        return self.__jobs_repository.get_all_jobs()

    def get_job_by_id(self, job_id: int) -> JobEntity | None:
        return self.__jobs_repository.get_job_by_id(job_id)

    def create_job(self, job_input: JobCreationAPIModel) -> JobEntity:
        creation_time = datetime.now()
        fields = {
            "id": 0,  # dummy value, need value to create JobEntity
            "created_date": creation_time,
            "last_modified": creation_time,
        }
        new_job = JobEntity(**fields, **job_input.dict())
        return self.__jobs_repository.create_job(new_job)
        # this object includes database-created id

    def delete_job(self, job_id: int) -> bool:
        return self.__jobs_repository.delete_job(job_id)

    def update_job(self, job_id: int, job_update_model: JobUpdateAPIModel) -> JobEntity | None:
        update_time = datetime.now()
        stored_job = self.get_job_by_id(job_id)
        if stored_job:
            # don't include in the dict the model fields that had no value in job_update_model
            update_data = job_update_model.dict(exclude_unset=True)
            update_data["last_modified"] = update_time
            updated_job = stored_job.copy(update=update_data)
            return self.__jobs_repository.update_job(job_id, updated_job)
        return None

        # stored_job = db[job_id]  # stored_job_model = JobEntity(**stored_job)
        # update_data = job_update.dict(exclude_unset=True)
        # # don't include in the dict the model fields that had no value in job_update object
        # print(
        #     "update_data dict wo exclude_unset: \n",
        #     job_update.dict(exclude_unset=False),
        # )
        # print("update data dict: \n", update_data)
        # update_data["last_modified"] = datetime.now()
        # updated_job = stored_job.copy(update=update_data)  # type -> JobEntity
        # print("updated_job:\n", updated_job)
        # db[job_id] = updated_job  # db[job_id] = jsonable_encoder(updated_job)
        # print("db[job_id]:\n", db[job_id])
        # return updated_job

    def load_data_at_startup(self) -> None:
        self.__jobs_repository.load_data_to_table()

    def delete_data_from_table(self) -> None:
        self.__jobs_repository.delete_data_from_table()
