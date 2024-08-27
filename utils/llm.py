import re
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline

def get_response(query):
    gpu_llm = HuggingFacePipeline.from_model_id(
        model_id="distilgpt2",  # Using a smaller model for testing
        task="text-generation",
        device=-1,  # -1 for CPU
        batch_size=1,  # Adjust based on resources
        model_kwargs={"temperature": 0.7, "max_length": 64, "do_sample": True},
    )

    gpu_chain = gpu_llm.bind(stop=["\n\n"])

    questions = [query]
    answers = gpu_chain.batch(questions)

    # Try to extract a numeric answer
    for answer in answers:
        print(f"Raw response: {answer}")
        numbers = re.findall(r'\b\d+\b', answer)
        if numbers:
            print(f"Extracted number: {numbers[0]}")
        else:
            print("No numeric answer found.")

if __name__ == "__main__":
    query = "What is 10+10?"
    get_response(query)
