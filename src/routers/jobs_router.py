from fastapi import APIRouter, HTTPException
from src.db_items import db_entities as db  # , db_last
from schemas.job_schemas import JobCreationAPIModel, JobUpdateAPIModel
from domain.job_entity import JobEntity
from typing import List, Dict

# from datetime import datetime
from services.jobs_services import JobsService

# from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/jobs", tags=["jobs"])

# @router.get("/")
# async def root():
#     return {"Hello": "World", "Name": "Mic"}


@router.get("/")
async def list_jobs() -> List[JobEntity]:
    return JobsService().get_all_jobs()
    # return list(db.values())


@router.get("/{job_id}")
async def get_job_by_id(job_id: int) -> JobEntity:
    job = JobsService().get_job_by_id(job_id)
    if job:
        return job
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")
    # if job_id in db:
    #     return db[job_id]


@router.post("/")
async def create_job(job_input: JobCreationAPIModel) -> JobEntity:
    return JobsService().create_job(job_input)


# # TODO: change the model to assign id in a better way,
# @router.post("/")
# async def create_job(job_input: JobCreationAPIModel) -> JobEntity:
#     creation_time = datetime.now()
#     global db_last
#     id = db_last + 1
#     db_last = id
#     fields = {
#         "id": id,
#         "created_date": creation_time,
#         "last_modified": creation_time,
#     }
#     new_job = JobEntity(**fields, **job_input.dict())
#     db[id] = new_job
#     return new_job


@router.delete("/{job_id}")
async def delete_job(job_id: int) -> Dict[str, str]:
    if JobsService().delete_job(job_id):
        return {"detail": f"Job with id {job_id} was deleted"}
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


@router.patch("/{job_id}")
async def update_job(job_id: int, job_update: JobUpdateAPIModel) -> JobEntity:
    updated_job = JobsService().update_job(job_id, job_update)
    if updated_job:
        return updated_job
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


# @router.patch("/{job_id}")
# async def update_job(job_update: JobUpdateAPIModel, job_id: int) -> JobEntity:
#     if job_id in db:
#         stored_job = db[job_id]  # stored_job_model = JobEntity(**stored_job)
#         update_data = job_update.dict(exclude_unset=True)
#         # don't include in the dict the model fields that had no value in job_update object
#         print(
#             "update_data dict wo exclude_unset: \n",
#             job_update.dict(exclude_unset=False),
#         )
#         print("update data dict: \n", update_data)
#         update_data["last_modified"] = datetime.now()
#         updated_job = stored_job.copy(update=update_data)  # type -> JobEntity
#         print("updated_job:\n", updated_job)
#         db[job_id] = updated_job  # db[job_id] = jsonable_encoder(updated_job)
#         print("db[job_id]:\n", db[job_id])
#         return updated_job
#     raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


def run():
    print(db[10], "\n")
    job_update = JobUpdateAPIModel(position="pos2", location="Center")
    res = update_job(10, job_update)
    print(res, "\n")
    print(f"updated_job type: {type(res)}\n")
    print(db[10], "\n")
    print(f"type in db: {type(db[10])}")
