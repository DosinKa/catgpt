import os
import google.generativeai as genai
from flask import Flask, request, render_template, jsonify

# Настройка Gemini AI
genai.configure(api_key="AIzaSyAdjmx5Fg68ORlWfETDOe4yKVMC3yzZJTc")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 819200,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-pro-exp-02-05",
    generation_config=generation_config,
    system_instruction="Answer every single question with just by meowing. No words just meow meow meow random number of times."
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "")
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(text)
    return jsonify({"ai_response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
