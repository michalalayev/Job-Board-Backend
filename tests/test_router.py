from fastapi.testclient import TestClient
from src.main import app
from db_items import db_entities as db, db_last
from fastapi.encoders import jsonable_encoder

client = TestClient(app)


def test_list_jobs():
    response = client.get("/v1/jobs")
    # response = <Response [200 OK]> -> type: httpx.Response
    # response.json() -> type: Dict or List[Dict]
    # list(db.values())[0] -> type: JobModel
    assert response.status_code == 200
    assert len(response.json()) == len(db)
    assert response.json() == jsonable_encoder(list(db.values()))


def test_get_job_by_id():
    response = client.get("/v1/jobs/0")
    assert response.status_code == 200
    job_in_db = jsonable_encoder(db[0])
    assert response.json() == job_in_db


def test_get_inexistent_job():
    job_id = 20
    response = client.get(f"v1/jobs/{job_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Job with id {job_id} does not exist"}


def test_update_job():
    response = client.patch(
        "v1/jobs/1",
        json={"position": "pos", "company": "comp", "location": "Center"},
    )
    assert response.status_code == 200
    assert response.json()["position"] == "pos"
    assert response.json()["company"] == "comp"
    response_get = client.get("v1/jobs/1")
    assert response.json() == response_get.json()


def test_update_job_empty_body():
    response = client.patch(
        "v1/jobs/1",
        json={},
    )
    assert response.status_code == 200
    assert response.json()["company"] == "Google"
    assert response.json()["position"] == "Fullstack Engineer"
    assert response.json()["last_modified"] >= jsonable_encoder(db[1].last_modified)


def test_create_job():
    response = client.post(
        "v1/jobs/",
        json={"position": "try1", "company": "try1", "location": "Tel Aviv"},
    )
    assert response.status_code == 200
    job_id = db_last + 1
    assert response.json()["id"] == job_id
    assert response.json()["position"] == "try1"
    assert response.json()["company"] == "try1"
    assert response.json()["location"] == "Tel Aviv"
    assert response.json()["created_date"] == response.json()["last_modified"]
    assert response.json()["status"] == "Wish List"
    response_get = client.get(f"v1/jobs/{job_id}")
    assert response_get.status_code == 200
    assert response_get.json()["id"] == job_id


def test_delete_job():
    job_id = 11
    response = client.delete(f"v1/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": f"Job with id {job_id} was deleted"}
    response_get = client.get(f"v1/jobs/{job_id}")
    assert response_get.status_code == 404
    assert response_get.json() == {"detail": f"Job with id {job_id} does not exist"}


def test_delete_inexistent_job():
    job_id = 11
    response = client.delete(f"v1/jobs/{job_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Job with id {job_id} does not exist"}


"""
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
