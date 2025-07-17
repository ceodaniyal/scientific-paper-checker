from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Dict
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4.1", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))

def suggest_improvements(state: Dict) -> Dict:
    suggestions = {}
    sections = state.get("sections", {})
    statuses = state.get("section_statuses", {})

    for name, content in sections.items():
        if statuses.get(name) != "unclear":
            continue

        prompt = ChatPromptTemplate.from_template("""
        The following {section_name} section was flagged as unclear. Suggest concrete improvements to make it more clear and complete.

        Text:
        \"\"\"{content}\"\"\"

        Suggestions:
        """)

        chain = prompt | llm
        response = chain.invoke({"section_name": name, "content": content})
        suggestions[name] = response.content.strip()

    state["suggestions"] = suggestions
    return state
