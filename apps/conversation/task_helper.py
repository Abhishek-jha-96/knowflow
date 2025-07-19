from huggingface_hub import InferenceClient
from apps.conversation.settings import HF_LLM_TOKEN

client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_LLM_TOKEN)

def query_llm(prompt):
    messages = [
            {"role": "user", "content": prompt}
        ]
        
    response = client.chat_completion(
        messages=messages,
        max_tokens=512,
        temperature=0.7
    )
    
    return response.choices[0].message.content
