from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
import numpy as np
from pymongo import MongoClient

client = MongoClient("mongodb+srv://anusha06:Akshat12!@cluster0.8ibtd.mongodb.net/?retryWrites=true&w=majority")
db = client["policy_database"]

treaties_collection = db["treaties"]


for treaty in db.treaties.find():
    treaty_embedding = model.encode(treaty["text"])
    db.treaties.update_one(
        {"_id": treaty["_id"]},
        {"$set": {"embedding": treaty_embedding.tolist()}}
    )

def find_similar_treaty(problem):
    problem_embedding = model.encode(problem)
    match = None
    high_similarity = -1
    for treaty in db.treaties.find():
        treaty_embedding = np.array(treaty["embedding"])
        similarity = np.dot(problem_embedding, treaty_embedding) / (
            np.linalg.norm(problem_embedding) * np.linalg.norm(treaty_embedding) )
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = treaty

    return best_match


