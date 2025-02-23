from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from pymongo import MongoClient
import os
import bcrypt

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__, template_folder="frontend")
app.secret_key = os.urandom(28)
MONGODB_URI = "mongodb+srv://anusha06:Akshat12!@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)

db = client["water_rights"]
users_collection = db["users"]
problems_collection = db["problems"]
treaties_collection = db["treaties"]
settlements_collection = db["settlements"]

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

    ai_response = llm_client.post(
        json = {"inputs": prompt, "parameters": {"max_new_tokens": 200}}
    )

    # Print the response for debugging
    print("AI Response:", ai_response)

    # Extract generated text
    generated_text = ai_response.get("generated_text", "No response generated")

    return jsonify({"petition": generated_text})


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
        return jsonify({"error": "incomplete form :()"}), 400

    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"success": False, "error": "username already exists :()"}), 409

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users_collection.insert_one({"username": username, "password": hashed_password})

    return jsonify({"success": True, "message": "registered succesfully :)"}), 201

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({"username": username})
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        return "Invalid username or password", 401
    session['username'] = username
    return jsonify({"success": True, "message": "Logged in"}), 200

@app.route("/submit", methods=["GET"])
def submit_page():
    return render_template("submit.html")

@app.route("/submit_problem", methods=["POST"])
def submit_problem_post():
    if 'username' not in session:
        return jsonify({"error": "User not logged in"}), 401
    title = request.form.get("title")
    description = request.form.get("description")
    category = request.form.get("category")

    if not title or not description:
        return jsonify({"error": "Form not fully completed"}), 400

    data = {
        "title": title,
        "description": description,
        "category": category,
        "user": session['username']
    }
    problems_collection.insert_one(data)
    return redirect(url_for("treaty_similarity", description=description))

sbert_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

@app.route("/treaty_similarity", methods=["GET", "POST"])
def treaty_similarity():
    problem_description = request.args.get("description") if request.method == "GET" else request.json.get("description")

    if not problem_description:
        return render_template("similar.html", treaty=None, similarity=0)
    
    problem_embedding = sbert_model.encode([problem_description])[0]
    best_match = None
    highest_similarity = -1

    for treaty in treaties_collection.find():
        treaty_embedding = np.array(treaty["embedding"])
        similarity = cosine_similarity([problem_embedding], [treaty_embedding])[0][0]

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = treaty

    return render_template("similar.html", treaty=best_match, similarity=round(highest_similarity * 100, 2))

if __name__ == '__main__':
    app.run(debug=True)
