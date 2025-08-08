import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM

load_dotenv()

def get_granite_llm():
    return WatsonxLLM(
        model_id=os.getenv("IBM_MODLE_ID"),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        apikey = os.getenv("WATSONX_API_KEY"),
        url = os.getenv("WATSONX_URL"),
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 100
        }
    )