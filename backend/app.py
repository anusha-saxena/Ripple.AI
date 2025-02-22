from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.water_rights
problems_collection = db.problems

# ✅ Add a homepage route to test if the server is running
@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

# Existing POST route for submitting problems
@app.route("/submit_problem", methods=["POST"])
def submit_problem():
    data = request.json
    problems_collection.insert_one(data)
    return jsonify({"client_message": data}), 200

if __name__ == "__main__":
    app.run(debug=True)
