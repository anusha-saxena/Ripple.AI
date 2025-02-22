import os
from huggingface_hub import InferenceClient, login

hf_token = os.getenv("HF_TOKEN") 
login(token=hf_token)

llm_client = InferenceClient(
    model="sentence-transformers/all-mpnet-base-v2",
    token=os.getenv("HF_TOKEN"), 
    timeout=200
)

def get_embeddings(inference_client: InferenceClient, text: str):
    response = inference_client.feature_extraction(text)
    return response 

#sample usage
response = get_embeddings(llm_client, "What is happiness?")
print(response)
