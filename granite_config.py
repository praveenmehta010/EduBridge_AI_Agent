# import os
# from dotenv import load_dotenv
# from langchain_ibm import WatsonxLLM

# load_dotenv()

# def get_granite_llm():
#     return WatsonxLLM(
#         model_id=os.getenv("IBM_MODLE_ID"),
#         project_id=os.getenv("WATSONX_PROJECT_ID"),
#         apikey = os.getenv("WATSONX_API_KEY"),
#         url = os.getenv("WATSONX_URL"),
#         params={
#             "decoding_method": "greedy",
#             "max_new_tokens": 100
#         }
#     )

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM

load_dotenv()

def get_env(key: str):
    """Try to get from Streamlit secrets, then from environment."""
    return st.secrets.get(key) or os.getenv(key)

def get_granite_llm():
    return WatsonxLLM(
        model_id=get_env("IBM_MODLE_ID"),
        project_id=get_env("WATSONX_PROJECT_ID"),
        apikey=get_env("WATSONX_API_KEY"),
        url=get_env("WATSONX_URL"),
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 100
        }
    )
