from flask import Flask, request, jsonify, render_template
from agents.orchestrator import OrchestratorAgent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
orchestrator = OrchestratorAgent()

@app.route('/')
def index():
    gemini_key = os.environ.get("GEMINI_KEY", "")
    return render_template('index.html', gemini_key=gemini_key)

@app.route('/upload', methods=['POST'])
def upload_image():
    # TODO: Handle file upload and pass path to orchestrator
    image_path = "mock/path/to/image.jpg"
    result = orchestrator.process_initial_upload(image_path)
    return jsonify(result)

@app.route('/edit', methods=['POST'])
def edit_image():
    # TODO: Handle live canvas updates via edit workflow
    data = request.json
    return jsonify({"status": "success", "data": data})

@app.route('/export', methods=['POST'])
def export_image():
    # TODO: Invoke export agent
    data = request.json
    return jsonify({"status": "exported", "download_url": "/path/to/file.pdf"})

if __name__ == '__main__':
    app.run(debug=True)
