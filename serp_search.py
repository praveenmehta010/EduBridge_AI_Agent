import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def get_courses(topic):
    params = {
        "engine": "google",
        "q": f"{topic} free online course site:coursera.org OR site:edx.org OR site:udemy.com",
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    links = []

    for r in results.get("organic_results", [])[:10]:
        link = r.get("link")
        title = r.get("title", "").lower()
        links.append(link)

        if len(links) > 4:
            break

    return links