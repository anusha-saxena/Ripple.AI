from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load SBERT model
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

#sample texts
text1 = "We promise $5M dollars."
text2 = "We gave out $2M dollars."

embedding1 = model.encode([text1])
embedding2 = model.encode([text2])

similarity_score = cosine_similarity(embedding1, embedding2)[0][0]

print(f"Similarity Score: {similarity_score:.4f}")  # Output: Similarity score between texts

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])

feature_names = np.array(vectorizer.get_feature_names_out())
tfidf_array = tfidf_matrix.toarray()

top_words_text1 = feature_names[np.argsort(tfidf_array[0])[-3:]]  # Top 3 words in text1
top_words_text2 = feature_names[np.argsort(tfidf_array[1])[-3:]]  # Top 3 words in text2

def explain_similarity(text1, text2, similarity_score, words1, words2):
    explanation = f"The two texts are {similarity_score*100:.1f}% similar.\n"

    if similarity_score > 0.8:
        explanation += "They express very similar ideas."
    elif similarity_score > 0.5:
        explanation += "They are somewhat related but differ in emphasis."
    else:
        explanation += "They discuss different topics."

    explanation += "\n\n**Key Differences:**"
    explanation += f"\n - '{text1}' emphasizes: {', '.join(words1)}."
    explanation += f"\n - '{text2}' focuses on: {', '.join(words2)}."

    return explanation

explanation = explain_similarity(text1, text2, similarity_score, top_words_text1, top_words_text2)
print(explanation)
