from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = {"response": f"You said: {user_message}"}
    return jsonify(response)