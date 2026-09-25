from flask import Blueprint, jsonify
from sqlalchemy import select

from .extensions import db
from .models import Team, Stops

health_bp = Blueprint("health", __name__)
team_bp = Blueprint("team", __name__)
stops_bp = Blueprint("stops", __name__)

@stops_bp.get("/stops")
def get_stops():
    if stops is None
        return jsonify({"error": "No stops found"}), 404
    return jsonify({"imageURL": stops.imageURL, "id": stops.id, "name": stops.name, "x": stops.x, "y": stops.y, 'tranfer': "yes" if stop.transfer else "no", 'wheelAccessible': "yes" if stop.wheelAccessible else "no", 'shelter': "yes" if stop.shelter else "no", 'bench': "yes" if stop.bench else "no", 'display': "yes" if stop.display else "no",  'ticketMachine': "yes" if stop.tikcetMachine else "no"}), 200
                    
@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@team_bp.get("/team")
def team_info():
    team = db.session.execute(select(Team)).scalars().first()
    if team is None:
        return jsonify({"error": "no team"}), 404
    return jsonify({"name": team.name, "members": team.members}), 200
