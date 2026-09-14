from typing import Any, TypedDict

from flask import Blueprint, jsonify, request
from sqlalchemy import select

from .extensions import db

health_bp = Blueprint("health", __name__)
@health_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200
