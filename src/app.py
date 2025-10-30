"""
Author: Kaleb Mohr
Date: 29 Oct 2025
Purpose: This is a lab web app to be used throughout the DevOps labs within the
Cisco Certified DevNet Associate course.
"""

import json
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    """Return data from the db.json file over the webpage."""
    with open('db.json', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
