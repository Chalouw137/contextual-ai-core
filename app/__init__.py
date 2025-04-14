import os
from flask import Flask, request, jsonify, Response, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    @app.route('/')
    def index():
        return send_from_directory(app.template_folder, 'index.html')

    @app.route('/chat', methods=['POST'])
    def chat():
        user_message = request.json.get('message')

        def generate():
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}],
                stream=True,
            )
            for chunk in completion:
                content = chunk.choices[0].delta.get("content", "")
                yield content

        return Response(generate(), content_type='text/plain')

    return app
