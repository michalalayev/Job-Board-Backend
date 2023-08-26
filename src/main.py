from fastapi import FastAPI
from routers import jobs_router
from services.jobs_services import JobsService
from database import create_db_and_tables, delete_tables

app = FastAPI()

app.include_router(jobs_router.router, prefix="/v1")


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    create_db_and_tables()
    JobsService().load_data_at_startup()


@app.on_event("shutdown")
def shutdown_event():
    delete_tables()
