def register_socket_events(socketio):
    @socketio.on("message")
    def handle_message(data):
        print("Received message:", data)
        socketio.emit("response", {"data": f"Echo: {data}"})
