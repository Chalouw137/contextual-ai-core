from flask import Flask
from flask_socketio import SocketIO
from .routes import main
from .sockets import socketio

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.register_blueprint(main)
    socketio.init_app(app, cors_allowed_origins="*")
    return app
