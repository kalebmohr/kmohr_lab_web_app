"""
Author: Kaleb Mohr
Date: 29 Oct 2025
Purpose: This is a lab web app to be used throughout the DevOps labs within the
Cisco Certified DevNet Associate course.
Last Modified: 30 Oct 2025
"""

import json
from flask import Flask, request, jsonify, render_template_string


app = Flask(__name__)

# Load employee data
with open("db.json", "r", encoding="utf-8") as file:
    data = json.load(file)
employees = data["employees"]

# Simple HTML for testing
HTML_PAGE = """
<!doctype html>
<html>
<head><title>Employee Lookup</title></head>
<body>
    <h2>Employee Lookup</h2>

    <form action="/check_title" method="post">
        <label>Enter Employee Name:</label>
        <input type="text" name="name" required>
        <button type="submit">Check Title</button>
    </form>

    <form action="/check_salary" method="post" style="margin-top:20px;">
        <label>Enter Employee Name:</label>
        <input type="text" name="name" required>
        <button type="submit">Check Salary</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    """Display the form page."""
    return render_template_string(HTML_PAGE)

@app.route("/check_title", methods=["POST"])
def check_title():
    """Return job title for a given employee."""
    name = request.form.get("name", "").strip().lower()
    for emp in employees:
        if emp["name"].lower() == name:
            return jsonify({"employee": emp["name"], "title": emp["title"]})
    return jsonify({"error": "Employee not found"}), 404

@app.route("/check_salary", methods=["POST"])
def check_salary():
    """Return salary for a given employee."""
    name = request.form.get("name", "").strip().lower()
    for emp in employees:
        if emp["name"].lower() == name:
            return jsonify({"employee": emp["name"], "salary": emp["salary"]})
    return jsonify({"error": "Employee not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
