from flask import Flask, render_template, request, jsonify
from google.cloud import speech
import vertexai
from vertexai.preview.generative_models import GenerativeModel

app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")
model = GenerativeModel("gemini-1.5-pro")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_code", methods=["POST"])
def generate_code():
    user_text = request.json.get("text")

    prompt = f"""
    Convert the following Hinglish or English voice instruction into correct code.
    Also return only code, no explanation.

    Instruction: {user_text}
    """

    response = model.generate_content(prompt)
    code = response.text

    return jsonify({"code": code})

if __name__ == "__main__":
    app.run(debug=True)
