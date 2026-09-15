from flask import Blueprint, jsonify
from sqlalchemy import select

from .extensions import db
from .models import Team

health_bp = Blueprint("health", __name__)
team_bp = Blueprint("team", __name__)


@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@team_bp.get("/team")
def team_info():
    team = db.session.execute(select(Team)).scalars().first()
    if team is None:
        return jsonify({"error": "no team"}), 404
    return jsonify({"name": team.name, "members": team.members}), 200
