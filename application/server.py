from flask import Flask
from flask_restful import Api
from flask_cors import CORS

server = None
api = None


def init(*args, **kwargs):
    global server
    global api

    server = Flask(__name__)
    CORS(server)

    api = Api(server)
    api.app.config['RESTFUL_JSON'] = {'ensure_ascii': False}
    api.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    from application.routes import init_routes
    init_routes()

    return server
