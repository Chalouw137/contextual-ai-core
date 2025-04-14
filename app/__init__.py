from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .sockets import socket_events
    socket_events(socketio)
    socketio.init_app(app)
    return app
