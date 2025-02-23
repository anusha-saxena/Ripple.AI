from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__, template_folder='templates')

MONGODB_URI = "mongodb+srv://anusha06:Akshat12!@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)

db = client["policy_database"]
treaties_collection = db["treaties"]

sbert_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

@app.route("/treaty_similarity", methods=["POST"])
def treaty_similarity():
    data = request.json
    problem_description = data.get("description")
    if not problem_description:
        return jsonify({"error": "No issue description provided"}), 400

    problem_embedding = sbert_model.encode([problem_description])[0]
    best_match = None
    highest_similarity = -1

    for treaty in treaties_collection.find():
        treaty_embedding = np.array(treaty["embedding"])
        similarity = cosine_similarity([problem_embedding], [treaty_embedding])[0][0]
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = treaty

    if best_match:
        return render_template("similar.html", treaty=best_match, similarity=round(highest_similarity * 100, 2))
    else:
        return render_template("similar.html", treaty=None, similarity=0)

if __name__ == '__main__':
    app.run(debug=True)
