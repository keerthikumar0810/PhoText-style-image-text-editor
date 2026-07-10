from flask import Flask, request, jsonify, render_template
from agents.orchestrator import OrchestratorAgent
import os
from dotenv import load_dotenv

load_dotenv()

from models.database import db
from models.image_record import ImageRecord

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

orchestrator = OrchestratorAgent()
@app.route('/')
def index():
    gemini_key = os.environ.get("GEMINI_KEY", "")
    return render_template('index.html', gemini_key=gemini_key)

@app.route('/upload', methods=['POST'])
def upload_image():
    # TODO: Handle file upload and pass path to orchestrator
    image_path = "mock/path/to/image.jpg"
    
    # Log to DB
    new_record = ImageRecord(original_image_path=image_path)
    db.session.add(new_record)
    db.session.commit()
    
    result = orchestrator.process_initial_upload(image_path)
    result["record_id"] = new_record.id
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
