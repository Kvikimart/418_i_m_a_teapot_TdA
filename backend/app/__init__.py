from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db, migrate
from .routes import health_bp, team_bp
from .models import Team


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}})

    app.register_blueprint(health_bp, url_prefix="/api/v1")
    app.register_blueprint(team_bp, url_prefix="/api/v1")

    @app.cli.command("seed")
    def seed():
        if not Team.query.first():
            my_team = Team(
                name="418 I'm a teapot",
                members="Viktor Vedral, Klára Tipplová, Matyáš Baloun",
            )
            db.session.add(my_team)
            db.session.commit()
            print("Seed proběhl.")
        else:
            print("Data už existují, seed přeskočen.")

    return app