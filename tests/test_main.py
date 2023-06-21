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


def test_get_job_by_id():
    response = client.get("/v1/jobs/0")
    assert response.status_code == 200
    job_in_db = db[0].dict()
    job_in_db["last_modified"] = str(job_in_db["last_modified"]).replace(" ", "T")
    job_in_db["created_date"] = str(job_in_db["created_date"]).replace(" ", "T")
    assert response.json() == job_in_db


"""
def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_read_inexistent_item():
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}
"""
