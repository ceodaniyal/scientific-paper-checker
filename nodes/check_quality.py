from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Dict
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4.1", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

def check_section_quality(state: Dict) -> Dict:
    sections = state.get("sections", {})
    section_statuses = {}

    for name, content in sections.items():
        if not content:
            section_statuses[name] = "missing"
            continue

        prompt = ChatPromptTemplate.from_template("""
        Evaluate the clarity and completeness of the following {section_name} section in a research paper.

        Text:
        \"\"\"{content}\"\"\"

        Classify this section as:
        - good (clear and complete)
        - unclear (present but vague or poorly written)

        Answer with only one word: good, unclear, or missing.
        """)

        chain = prompt | llm
        response = chain.invoke({"section_name": name, "content": content})
        classification = response.content.strip().lower()
        section_statuses[name] = classification

    state["section_statuses"] = section_statuses

    # If any are missing, return that route
    if "missing" in section_statuses.values():
        return {"route": "missing", **state}
    elif "unclear" in section_statuses.values():
        return {"route": "unclear", **state}
    else:
        return {"route": "good", **state}
