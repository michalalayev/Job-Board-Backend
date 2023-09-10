from fastapi import FastAPI
from routers import jobs_router
from services.jobs_services import JobsService
from database import create_db_and_tables  # , delete_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobs_router.router, prefix="/v1")


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    create_db_and_tables()
    JobsService().load_data_at_startup()


# enable only when want to restart the table.
# On every reload there is a shutdown event, so if it's enabled all the time,
# the table is deleted on every change of the code.
# @app.on_event("shutdown")
# def shutdown_event():
#     delete_tables()
