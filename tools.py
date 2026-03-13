from langchain.tools import tool
from rag import build_vector_store
import pandas as pd

COMPANY_PATH = "data/companies.csv"


vectorstore = build_vector_store()


@tool
def rag_job_search(resume_text: str) -> str:
    """
    Retrieve relevant jobs from vector database using resume content.
    """

    docs = vectorstore.similarity_search(resume_text, k=3)

    jobs = [doc.page_content for doc in docs]

    return "\n\n".join(jobs)


@tool
def company_recommender(role: str) -> str:
    """
    Suggest companies hiring for the role.
    """

    df = pd.read_csv(COMPANY_PATH)

    row = df[df["role"].str.lower() == role.lower()]

    if row.empty:
        return "No company data found."

    companies = row.iloc[0]["companies"]

    return f"Top companies hiring {role}: {companies}"