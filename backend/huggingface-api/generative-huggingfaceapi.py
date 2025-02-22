import os
from huggingface_hub import InferenceClient, login

os.environ["HF_TOKEN"] = "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"
login()

hf_token = os.getenv("HF_TOKEN") 
login(token=hf_token)

llm_client = InferenceClient(
    model="microsoft/Phi-3-mini-4k-instruct",
    token=os.getenv("HF_TOKEN"),
    timeout=200
)

def call_llm(inference_client: InferenceClient, prompt: str): 
    response = inference_client.text_generation(
        prompt,
        max_new_tokens=200
    )
    return response

#sample usage
response = call_llm(llm_client, "I need help with writing a short petition to get clean water in my community?")
print(response)