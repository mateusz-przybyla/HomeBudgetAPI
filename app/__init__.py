from flask import Flask

from app.config import Config
from app.extensions import api, db

from app.expense import blp as ExpenseBlueprint

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    api.init_app(app)

    api.register_blueprint(ExpenseBlueprint)

    return app

