from fastapi import FastAPI
from routers import jobs_router
from services.jobs_services import IJobsService, JobsService

app = FastAPI()

app.include_router(jobs_router.router, prefix="/v1")


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup_event():
    JobsService().load_data_at_startup()

