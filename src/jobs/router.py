from fastapi import APIRouter, HTTPException
from .db_items import db, db_last
from .schemas import JobModel, JobInputModel, JobUpdateModel
from typing import List, Dict
from datetime import datetime

# from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/")
async def root():
    return {"Hello": "World", "Name": "Mic"}


@router.get("/v1/jobs")
async def list_jobs() -> List[JobModel]:
    return list(db.values())


@router.get("/v1/jobs/{job_id}")
async def get_job_by_id(job_id: int) -> JobModel:
    if job_id in db:
        return db[job_id]
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


# TODO: change the model to assign id in a better way,
@router.post("/v1/jobs")
async def create_job(job_input: JobInputModel) -> JobModel:
    creation_time = datetime.now()
    global db_last
    id = db_last + 1
    db_last = id
    fields = {
        "id": id,
        "created_date": creation_time,
        "last_modified": creation_time,
    }
    new_job = JobModel(**fields, **job_input.dict())
    db[id] = new_job
    return new_job


@router.delete("/v1/jobs/{job_id}")
async def delete_job(job_id: int) -> Dict[str, str]:
    if job_id in db:
        db.pop(job_id)
        return {"detail": f"Job with id {job_id} was deleted"}
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


@router.patch("/v1/jobs/{job_id}")
async def update_job(job_update: JobUpdateModel, job_id: int) -> JobModel:
    if job_id in db:
        stored_job = db[job_id]  # stored_job_model = JobModel(**stored_job)
        update_data = job_update.dict(exclude_unset=True)
        # don't include in the dict the model fields that didn't have value in the job_update object
        print("update data dict: \n", update_data)
        update_data["last_modified"] = datetime.now()
        updated_job = stored_job.copy(update=update_data)  # type -> JobModel
        print("updated_job:\n", updated_job)
        db[job_id] = updated_job  # db[job_id] = jsonable_encoder(updated_job)
        print("db[job_id]:\n", db[job_id])
        return updated_job
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


def run():
    print(db[10], "\n")
    job_update = JobUpdateModel(position="pos2", location="Center")
    res = update_job(job_update, 10)
    print(res, "\n")
    print(f"updated_job type: {type(res)}\n")
    print(db[10], "\n")
    print(f"type in db: {type(db[10])}")
