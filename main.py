from utils.pdf_utils import extract_text_from_pdf
from langgraph_flow import scientific_graph
import uuid

pdf_path = "data/Imaizumi-Yuko_Research-paper-2017.pdf"
text = extract_text_from_pdf(pdf_path)

paper_id = str(uuid.uuid4())
input_data = {"paper_id": paper_id, "text": text}

scientific_graph.invoke(input_data)
