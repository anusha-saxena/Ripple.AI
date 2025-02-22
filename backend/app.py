from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import os
import bcrypt

app = Flask(__name__, template_folder = "frontend")

MONGODB_URI = "mongodb+srv://anushasaxena06:QkVhYP3MT0WAhz5B@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
#added databases in mongoDB Atlas basically
db = client["water_rights"]
users_collection = db["users"]
problems_collection = db["problems"]

@app.route("/")
def home():
    return "Flask server running :)"

#login page
@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")  #link to html login page

#user registration
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if users_collection.find_one({"username": username}):
        return jsonify({"error": "Username already exists"}), 409

    #hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #database insert
    users_collection.insert_one({
        "username": username,
        "password": hashed_password.decode('utf-8')  #store as string
    })

    return jsonify({"message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.form 
    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({"username": username})
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        return "Invalid username or password", 401

    return "Login successful"





#SUBMISSION FORM!

@app.route("/submit", methods=["GET"])
def submit_page():
    return render_template("submit.html")

@app.route("/submit_problem", methods=["POST"])
def submit_problem_post():
    title = request.form.get("title")
    description = request.form.get("description")
    category = request.form.get("category")
    if not title or not description:
        return jsonify({"error": "not fully completed :("}), 400
    #insertingggg to mongo!
        result = problems_collection.insert_one({
        "title": title,
        "description": description,
        "category": category
    })
    return jsonify({"message": "submitted successfully :)"}), 200

if __name__ == '__main__':
    app.run(debug=True)


