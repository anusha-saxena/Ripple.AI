from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
app = Flask(__name__)
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.water_rights
problems_collection = db.problems

@app.route("/submit_problem", methods=["POST"])
def submit_problem():
    data = request.json
    problems_collection.insert_one(data)
    return jsonify({"client_message": data}), 200


if __name__ == "__main__":
    app.run(debug=True)