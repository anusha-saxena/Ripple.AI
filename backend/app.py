from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
#
app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.water_rights
problems_collection = db.problems

@app.route("/", methods=["GET"])
def home():
    return "Flask server running :)"

@app.route("/submit_problem", methods=["POST"])
def submit_problem():
    data = request.json
    problems_collection.insert_one(data)
    return jsonify({"client_message": data}), 200

@app.route('/get', methods=['GET'])
def get_documents():
    documents = list(collection.find({}, {"_id": 0}))
    return jsonify(documents)

if __name__ == '__main__':
    app.run(debug=True)
