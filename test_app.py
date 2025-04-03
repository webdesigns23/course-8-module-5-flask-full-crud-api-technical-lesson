from app import app
import store

def reset_data():
    store.events.clear()
    store.next_id = 1

def test_create_event():
    reset_data()
    client = app.test_client()
    response = client.post("/events", json={"title": "New Event"})
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data and "title" in data
    assert data["title"] == "New Event"

def test_get_event():
    reset_data()
    client = app.test_client()
    client.post("/events", json={"title": "Sample Event"})
    response = client.get("/events/1")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Sample Event"

def test_patch_event():
    reset_data()
    client = app.test_client()
    client.post("/events", json={"title": "Old Title"})
    response = client.patch("/events/1", json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.get_json()["title"] == "Updated Title"

def test_delete_event():
    reset_data()
    client = app.test_client()
    client.post("/events", json={"title": "To Be Deleted"})
    response = client.delete("/events/1")
    assert response.status_code == 204
    get_response = client.get("/events/1")
    assert get_response.status_code == 404
