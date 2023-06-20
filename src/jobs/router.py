from fastapi import APIRouter, HTTPException
from .db_items import db
from .models import JobModel, JobInputModel, JobUpdateModel
from typing import List, Dict
from datetime import datetime

# from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/")
async def root():
    print(type(db[0].dict()))
    print(type(db[0]))
    return {"Hello": "World", "Name": "Mic"}


# TODO: change the function name to List method
@router.get("/v1/jobs")
async def get_jobs() -> List[JobModel]:
    return list(db.values())


# TODO: change the function name to get by method
@router.get("/v1/jobs/{job_id}")
async def get_job_by_id(job_id: int) -> JobModel:
    if job_id in db:
        return db[job_id]
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


# TODO: - change the model to assign id in a better way,
#       - check if working
@router.post("/v1/jobs")
async def create_job(job_input: JobInputModel) -> JobModel:
    creation_time = datetime.now()
    id = len(db)
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
        stored_job = db[job_id]
        # stored_job_model = JobModel(**stored_job)
        update_data = job_update.dict(exclude_unset=True)  # exclude default values
        update_data["last_modified"] = datetime.now()
        updated_job = stored_job.copy(update=update_data)
        db[job_id] = updated_job
        # db[job_id] = jsonable_encoder(updated_job)
        return updated_job
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


