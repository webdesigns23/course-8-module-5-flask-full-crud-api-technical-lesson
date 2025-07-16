from flask import Flask, request, jsonify, abort
from store import events  # Shared in-memory storage for events

app = Flask(__name__)

#Class to Represent events
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# TODO: Task 1 - Define the Problem
# Create an event with a unique ID and a title
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # TODO: Task 4 - Return and Handle Results
    data = request.get_json()
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(id=new_id, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Retrieve a single event by its ID
@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 4 - Return and Handle Results
    def get_event(id):
        event = next((e for e in events if e.id == id), None)
        return jsonify(event.to_dict()) if event else ("Event not found", 404)

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # TODO: Task 4 - Return and Handle Results
    data = request.get_json()
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    if "title" in data:
        event.title = data["title"]
    return jsonify(event.to_dict())

# TODO: Task 1 - Define the Problem
# Delete an event by its ID
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # TODO: Task 4 - Return and Handle Results
    global events
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    events = [e for e in events if e.id != id]
    return ("Event deleted", 204)

if __name__ == "__main__":
    app.run(debug=True)
