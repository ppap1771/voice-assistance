import re
from transformers import pipeline
import transformers
import torch

def get_response(query):
    torch.set_default_device("cpu")

    model = transformers.AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)
    tokenizer = transformers.AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)

    inputs = tokenizer(query, return_tensors="pt", return_attention_mask=False)

    outputs = model.generate(**inputs, max_length=200)
    text = tokenizer.batch_decode(outputs)
    return text

if __name__ == "__main__":
    # query = "What is 10+10?"
    out = get_response("10+10 = ?")
