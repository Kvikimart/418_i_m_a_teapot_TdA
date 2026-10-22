from flask import Blueprint, jsonify, request
from sqlalchemy import select

from .extensions import db
from .models import Team, Stops

health_bp = Blueprint("health", __name__)
team_bp = Blueprint("team", __name__)
stops_bp = Blueprint("stops", __name__)

REQUIRED_BOOL_FIELDS = ("wheelchair_accessible", "has_shelter", "has_ticket_machine")


def parse_stop_input(data):
    """Validate a StopInput body. Returns (fields, error)."""
    if not isinstance(data, dict):
        return None, "Body must be a JSON object"

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        return None, "'name' is required and must be a non-empty string"
    if len(name) > 128:
        return None, "'name' must be at most 128 characters"

    fields = {"name": name}
    for key in REQUIRED_BOOL_FIELDS:
        if not isinstance(data.get(key), bool):
            return None, f"'{key}' is required and must be a boolean"
        fields[key] = data[key]

    image_url = data.get("image_url")
    if image_url is not None and not isinstance(image_url, str):
        return None, "'image_url' must be a string or null"
    if image_url is not None and len(image_url) > 255:
        return None, "'image_url' must be at most 255 characters"
    fields["image_url"] = image_url or None

    return fields, None


def stop_or_404(stop_id):
    stop = db.session.get(Stops, stop_id)
    if stop is None:
        return None, (jsonify({"error": "Stop not found"}), 404)
    return stop, None


@stops_bp.get("/stops")
def get_stops():
    stops = db.session.execute(select(Stops).order_by(Stops.id)).scalars().all()
    return jsonify([stop.to_dict() for stop in stops]), 200


@stops_bp.post("/stops")
def create_stop():
    fields, error = parse_stop_input(request.get_json(silent=True))
    if error:
        return jsonify({"error": error}), 400

    stop = Stops(**fields)
    db.session.add(stop)
    db.session.commit()
    return jsonify(stop.to_dict()), 201


@stops_bp.get("/stops/<int:stop_id>")
def get_stop(stop_id):
    stop, error = stop_or_404(stop_id)
    if error:
        return error
    return jsonify(stop.to_dict()), 200


@stops_bp.put("/stops/<int:stop_id>")
def update_stop(stop_id):
    stop, error = stop_or_404(stop_id)
    if error:
        return error

    fields, error = parse_stop_input(request.get_json(silent=True))
    if error:
        return jsonify({"error": error}), 400

    for key, value in fields.items():
        setattr(stop, key, value)
    db.session.commit()
    return jsonify(stop.to_dict()), 200


@stops_bp.delete("/stops/<int:stop_id>")
def delete_stop(stop_id):
    stop, error = stop_or_404(stop_id)
    if error:
        return error

    db.session.delete(stop)
    db.session.commit()
    return "", 204


@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@team_bp.get("/team")
def team_info():
    team = db.session.execute(select(Team)).scalars().first()
    if team is None:
        return jsonify({"error": "no team"}), 404
    return jsonify({"name": team.name, "members": team.members}), 200

