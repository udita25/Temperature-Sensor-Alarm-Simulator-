
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Simulating here, but in real-time this would be replaced with a proper database
def get_last_temperature_reading():
    try:
        with open('temperature_data.json', 'r') as f:
            data = json.load(f)
            return data[-1] if data else None
    except FileNotFoundError:
        return None

@app.route('/temperature', methods=['GET'])#API expose a single route to issue GET request to get most recent readings
def get_temperature():
    last_reading = get_last_temperature_reading()
    if last_reading:
        return jsonify(last_reading), 200#HTTP Status Code(ok)
    else:
        return jsonify({"error": "No temperature data available"}), 404#Http Status code(error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)