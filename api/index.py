import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load marks data
with open('marks.json', 'r') as f:
    marks_data = json.load(f)


@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get 'name' parameters from query
    results = [entry['marks'] for entry in marks_data if entry['name'] in names]
    return jsonify({"marks": results})


# Export the app for Vercel
app = app
