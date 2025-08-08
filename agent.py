from langgraph.graph import StateGraph, END
from granite_config import get_granite_llm
from serp_search import get_courses
from typing import TypedDict
import json

llm = get_granite_llm()

class AgentState(TypedDict):
    user_input: str
    topic: str
    level: str
    courses: list[str]

def extract_info(state: AgentState) -> dict:
    user_input = state["user_input"]
    prompt = f"""Extract topic and level from this sentence:

"{user_input}"

Respond in JSON like:
{{
    "topic": "topic_name",
    "level": "beginner/intermediate/advanced"
}}
"""
    response = llm.invoke(prompt)

    if isinstance(response, str):
        json_start = response.find("{")
        json_end = response.rfind("}") + 1
        try:
            parsed = json.loads(response[json_start:json_end])
        except Exception:
            parsed = {"topic": "general", "level": "beginner"}
    else:
        parsed = response

    return {
        "topic": parsed.get("topic", "general"),
        "level": parsed.get("level", "beginner")
    }

def fetch_courses(state: AgentState) -> dict:
    topic = state["topic"]
    course_links = get_courses(topic)
    return {"courses": course_links}

def build_agent():
    builder = StateGraph(AgentState)

    builder.add_node("extract", extract_info)
    builder.add_node("fetch", fetch_courses)

    builder.set_entry_point("extract")
    builder.add_edge("extract", "fetch")
    builder.set_finish_point("fetch")

    return builder.compile()
