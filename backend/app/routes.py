from flask import Blueprint, jsonify, request, Flask
from sqlalchemy import select

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200

app = Flask(__name__)
app.register_blueprint(health_bp, url_prefix="/api/v1")
