from flask import Blueprint, jsonify
from sqlalchemy import select

from .extensions import db
from .models import Team, Stops

health_bp = Blueprint("health", __name__)
team_bp = Blueprint("team", __name__)
stops_bp = Blueprint("stops", __name__)
create_bp = Blueprint("create_stop", __name__)

@stops_bp.get("/stops")
def get_stops():
    stops = db.session.execute(select(Stops)).scalars().all()
    if not stops:
        return jsonify({"error": "No stops found"}), 404

    return jsonify(
        [
            {
                "id": stop.id,
                "name": stop.name,
                "lines": stop.lines,
                "is_transfer": stop.is_transfer,
                "transfer_lines": stop.transfer_lines,
                "x": float(stop.x),
                "y": float(stop.y),
                "wheelchair_accessible": stop.wheelchair_accessible,
                "has_shelter": stop.has_shelter,
                "has_bench": stop.has_bench,
                "has_ticket_machine": stop.has_ticket_machine,
                "has_display": stop.has_display,
                "image_url": stop.image_url,
            }
            for stop in stops
        ]
    ), 200
                    
@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@team_bp.get("/team")
def team_info():
    team = db.session.execute(select(Team)).scalars().first()
    if team is None:
        return jsonify({"error": "no team"}), 404
    return jsonify({"name": team.name, "members": team.members}), 200

