def socket_events(socketio):
    @socketio.on('message')
    def handle_message(msg):
        print('Received message: ' + msg)
        socketio.send(msg, broadcast=True)
