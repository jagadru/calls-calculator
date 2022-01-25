import flask
from flask_cors import CORS

from server.routes import calls_calculator_routes
from server.utils import config


class MainApp:
    instance = None

    def __init__(self):
        self.app = flask.Flask(__name__)
        CORS(self.app, support_credentials=True, automatic_options=True)

        self._init_call_calculator_routes()
        MainApp.instance = self.app

    def _init_call_calculator_routes(self):
        calls_calculator_routes.init(self.app)

    def get_flask_app(self):
        return self.app

    def start(self, debug=True):
        self.app.run(port=config.get_server_port(), debug=debug)


def wsgi(*args):
    return MainApp().instance(*args)
