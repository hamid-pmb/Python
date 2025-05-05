from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api', methods=['POST'])
def handle_request():
    data = request.get_json()
    text = data.get("text", "")
    if text == "1000":
        return jsonify({"message": "OK"})
    else:
        return jsonify({"message": "Invalid input"})

if __name__ == "__main__":
    app.run(debug=True)