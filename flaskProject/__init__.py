from flask import Flask
from .views.login import login

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login)
    return app