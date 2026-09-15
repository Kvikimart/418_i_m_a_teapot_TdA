from flask import Blueprint, jsonify, request, Flask
from sqlalchemy import select

health_bp = Blueprint("health", __name__)
team_bp = Blueprint("team", __name__)


@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200

app = Flask(__name__)
app.register_blueprint(health_bp, url_prefix="/api/v1")

@team_bp.get("/team")
def team_info():
    team = db.session.execute(select(Team)).scalars().first()
    if team is None:
        return jsonify({"error": "no team"}), 404
    return jsonify({"name": team.name, "members": team.members}), 200
