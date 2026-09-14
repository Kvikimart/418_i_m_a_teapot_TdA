from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db
from .routes import health_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}})

    app.register_blueprint(health_bp, url_prefix="/api/v1")

    return app
