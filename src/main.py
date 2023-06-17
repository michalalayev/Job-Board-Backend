from fastapi import FastAPI, HTTPException
from dbItems import db
from models import JobModel, JobInputModel, JobUpdateModel
from typing import List, Any
from datetime import datetime

app = FastAPI()


@app.get("/")
def root():
    print(type(db[0].dict()))
    print(type(db[0]))
    return {"Hello": "World", "Name": "Mic"}


# TODO: change the function name to List method
@app.get("/v1/jobs")
def get_jobs() -> List[JobModel]:
    return db


# TODO: change the function name to get by method
@app.get("/v1/jobs/{job_id}")
def get_job_by_id(job_id: int) -> JobModel:
    for job in db:
        if job.id == job_id:
            return job
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


# TODO: change the model to assign id in a better way,
#       check if working
@app.post("/v1/jobs")
def create_job(job_input: JobInputModel) -> JobModel:
    creation_time = datetime.now()
    fields = {
        "id": len(db),
        "created_date": creation_time,
        "last_modified": creation_time,
    }
    job = JobModel(**fields, **job_input.dict())
    db.append(job)
    return job


@app.delete("/v1/jobs/{job_id}")
def delete_job(job_id: int) -> None:
    for job in db:
        if job.id == job_id:
            db.remove(job)
            return
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


@app.patch("/v1/jobs/{job_id}")
def update_job(job_update: JobUpdateModel, job_id: int) -> Any:
    for job in db:
        if job.id == job_id:
            update_data = job_update.dict(exclude_unset=True)  # exclude default values
            job = job.copy(update=update_data)
            # TODO: the update does not show inside the object in the db - fix
            return job
    raise HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")


job_update = JobUpdateModel(position="pos3", location="Center")
res = update_job(job_update, 10)
print(res)
print(db[-1])
