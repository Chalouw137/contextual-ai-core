from flask_socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('connect')
def handle_connect():
    emit("response", {"message": "Connected to real-time AI!"})

@socketio.on('user_message')
def handle_message(data):
    user_input = data.get("message")
    emit("response", {"message": f"You said: {user_input}"})
