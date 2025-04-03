# Technical Lesson: Building a Full CRUD REST API with Flask

## Learning Goals

- Understand how HTTP methods map to CRUD operations in REST.
- Build Flask routes that handle POST, GET, PATCH, and DELETE requests.
- Work with structured JSON input and output.
- Use in-memory Python objects to simulate persistent data.
- Follow RESTful conventions in route naming, structure, and response codes.

## Introduction

Most modern applications need more than just data retrieval—they also require the ability to create, update, and delete resources. This is known as **Full CRUD**: Create, Read, Update, and Delete.

In this lesson, we will focus on:

- Building POST, PATCH, DELETE, and GET routes with Flask.
- Receiving and handling JSON input using `request.get_json()`.
- Structuring responses using Python objects and `jsonify()`.
- Returning appropriate HTTP status codes for each type of operation.

We’ll use an event management API as our example. This API will allow users to:

- View a specific event by ID.
- Create new events.
- Update event details like the title.
- Delete events that are no longer needed.

The current system:

- Uses an in-memory list of `Event` class instances.
- Simulates backend behavior without a database.
- Needs route handlers for full CRUD interactions.

We will walk through building this API step by step, expanding beyond read-only access into a complete backend experience.

## Code Along

### Setting Up the Project

To get started, clone the repository and install any dependencies.

If you're using `pipenv`:

```bash
git clone <repo-url>
cd flask-full-crud-api
pipenv install
pipenv shell
```

If you're using `pip`:

```bash
git clone <repo-url>
cd flask-full-crud-api
pip install -r requirements.txt
```

### Writing the Full CRUD API with Flask

We’ll define all routes inside `app.py` and simulate events with mock objects.

#### Example: `app.py`

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Event class
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# Mock event data
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# READ: Get event by ID
@app.route("/events/<int:id>", methods=["GET"])
def get_event(id):
    event = next((e for e in events if e.id == id), None)
    return jsonify(event.to_dict()) if event else ("Event not found", 404)

# CREATE: Add new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(id=new_id, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# UPDATE: Modify event title
@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    data = request.get_json()
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    if "title" in data:
        event.title = data["title"]
    return jsonify(event.to_dict())

# DELETE: Remove an event
@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    global events
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    events = [e for e in events if e.id != id]
    return ("Event deleted", 204)

if __name__ == "__main__":
    app.run(debug=True)
```

### Testing the API

Run the app using:

```bash
python app.py
```

Then visit or test the following endpoints:

- `GET /events/1` – Get a specific event  
- `POST /events` – Add a new event  
  - JSON body: `{ "title": "AI Conference" }`
- `PATCH /events/1` – Update an event title  
  - JSON body: `{ "title": "Updated Event Title" }`
- `DELETE /events/2` – Delete event with ID 2

You can test using your browser, Postman, or curl.

## Best Practices for Full CRUD APIs

- Use RESTful resource routes (`/events`, `/events/<id>`).
- Use JSON format for both requests and responses.
- Return proper status codes: 201 for created, 204 for deleted, 404 for not found.
- Avoid changing server state in GET requests.
- Structure all responses consistently using dictionaries and `jsonify()`.

## Conclusion

By building a Full CRUD REST API with Flask, developers can:

- Simulate complete backend functionality.
- Create routes that reflect real-world application logic.
- Connect APIs to frontends or testing tools like Postman.
- Prepare for integration with databases and advanced validation.

This lesson sets the stage for fully functional APIs and scalable backend systems.
