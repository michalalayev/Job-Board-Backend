from fastapi.testclient import TestClient
from src.main import app
from src.jobs.db_items import db

client = TestClient(app)


def test_get_jobs():
    response = client.get("/v1/jobs")
    ### original response: ###
    # type(response) = <class 'httpx.Response'>
    # response = <Response [200 OK]>
    ### json response: ###
    # type(response.json()) = <class 'list'>
    # type(response.json()[0]) = <class 'dict'>
    # type(list(db.values())[0]) = <class 'models.JobModel'>
    assert response.status_code == 200
    assert len(response.json()) == len(db)


# print(db[10], "\n")
# job_update = JobUpdateModel(position="pos2", location="Center")
# res = update_job(job_update, 10)
# print(res, "\n")
# print(f"updated_job type: {type(res)}\n")
# print(db[10], "\n")
# print(f"type in db: {type(db[10])}")
