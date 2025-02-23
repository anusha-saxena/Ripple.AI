from flask import Flask, jsonify, request, render_template, session
from pymongo import MongoClient
import os
import bcrypt
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__, template_folder = "frontend")
app.secret_key = os.urandom(28)
MONGODB_URI = "mongodb+srv://anusha06:Akshat12!@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)

db = client["water_rights"]
users_collection = db["users"]
problems_collection = db["problems"]

#huggingface api setup - generative 
HF_TOKEN = os.getenv("HF_TOKEN") 
llm_client = InferenceClient(
    model="microsoft/Phi-3-mini-4K-instruct",
    token=HF_TOKEN
)

#implement sbert for text similarity 
sbert_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

@app.route("/")
def home():
    return "Flask server running :)"

#ai generated petition
@app.route("/generate_petition", methods=["POST"])
def generate_petition():
    data = request.json
    issue_description = data.get("description")

    if not issue_description:
        return jsonify({"error": "No issue description provided"}), 400
    
    prompt = f"Write a short petition for the following social justice issue: {issue_description}"
    ai_response = llm_client.text_generation(prompt, max_new_tokens=200)

    return jsonify({"petition": ai_response})

#text comparison 
@app.route("/compare_texts", methods=["POST"])
def compare_texts():
    data = request.json
    text1 = data.get("text1")
    text2 = data.get("text2")

    if not text1 or not text2:
        return jsonify({"error": "Both texts are needed"}), 400

    #obtain the sbert embeddings
    embedding1 = sbert_model.encode([text1])
    embedding2 = sbert_model.encode([text2])

    similarity_score = cosine_similarity(embedding1, embedding2)[0][0] * 100 #compute percentage similarity 

    return jsonify({"similarity_score": round(similarity_score, 2)})

#user registration
@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")
@app.route("/register", methods=["POST"])
def register_post():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error":"no complete :("}), 400
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"success": False, "error": "Username already exists"}), 409
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
   #inserting into MONGODB Users Database!!!!! :>>
    data = {
        "username": username,
        "password": hashed_password
    }
    result = users_collection.insert_one(data)
    return jsonify({"success": True, "message": "Registered successfully"}), 201


#login page
@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")  #link to html login page


@app.route("/login", methods=["POST"])
def login():
    data = request.form 
    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({"username": username})
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        return "Invalid username or password", 401
    else:
        session['username'] = username
        return jsonify({"success": True, "message": "logged in :)"}), 200

    
    return "Login successful"

#SUBMISSION FORM!

@app.route("/submit", methods=["GET"])
def submit_page():
    return render_template("submit.html")

@app.route("/submit_problem", methods=["POST"])
def submit_problem_post():
    if 'username' not in session:
        return jsonify({"error": "user not logged in"}), 401

    title = request.form.get("title")
    description = request.form.get("description")
    category = request.form.get("category")
    user = session['username'] 
    if not title or not description:
        return jsonify({"error": "not fully completed :("}), 400
    #insertingggg to mongo!
    data = {
        "title": title,
        "description": description,
         "category": category,
         "user": user
    }
    result = problems_collection.insert_one(data)
    return jsonify({"message": "submitted successfully :)"}), 200

if __name__ == '__main__':
    app.run(debug=True)