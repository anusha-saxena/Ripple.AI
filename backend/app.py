from flask import Flask, jsonify, request
from pymongo import MongoClient
<<<<<<< Updated upstream
import os

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.water_rights
problems_collection = db.problems

@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

@app.route("/submit_problem", methods=["POST"])
def submit_problem():
    data = request.json
    problems_collection.insert_one(data)
    return jsonify({"client_message": data}), 200
=======

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["testdb"]  
collection = db["testcollection"]  

@app.route('/')
def home():
    return jsonify({"message": "Flask server is running!"})

@app.route('/add', methods=['POST'])
def add_document():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)})
>>>>>>> Stashed changes

@app.route('/get', methods=['GET'])
def get_documents():
    documents = list(collection.find({}, {"_id": 0}))
    return jsonify(documents)

if __name__ == '__main__':
    app.run(debug=True)
