from flask import Flask
from flask_socketio import SocketIO
from .routes import main
from .sockets import register_socket_events

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../.env", silent=True)
    app.register_blueprint(main)
    register_socket_events(socketio)
    socketio.init_app(app)
    return app
