from flask import Flask
from dash import Dash
import dash_bootstrap_components as dbc
from animal_dashboard.views.layout import serve_layout
from animal_dashboard.controllers.auth_controller import auth_blueprint
from animal_dashboard.config import Config

def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)
    server.register_blueprint(auth_blueprint)

    app = Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
    app.title = "Animal Shelter Dashboard"
    app.layout = serve_layout

    return app