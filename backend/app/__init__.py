from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db
from .routes import health_bp
from .models import Team

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}})

    app.register_blueprint(health_bp, url_prefix="/api/v1")

    with app.app_context():
        db.create_all()
       
        if not Team.query.first():
           
            my_team = Team(name="418 I'm a teapot", members=["Viktor Vedral", "Klára Tipplová" ,"Matyáš Baloun"]
            db.session.add(my_team)
            db.session.commit()

    return app
