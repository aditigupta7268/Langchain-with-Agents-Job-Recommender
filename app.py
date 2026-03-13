from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import PyPDF2

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

from tools import rag_job_search, company_recommender


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)


tools = [
    rag_job_search,
    company_recommender
]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are an AI career advisor.\n"
         "Use the RAG job search tool to find relevant jobs from the knowledge base.\n"
         "Then suggest companies hiring for those roles."
        ),

        ("human", "{input}"),

        ("placeholder", "{agent_scratchpad}")
    ]
)


agent = create_tool_calling_agent(
    llm,
    tools,
    prompt
)


agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


def extract_pdf_text(file):

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text[:5000]


def get_recommendation(resume_text):

    query = f"""
Analyze this resume and recommend relevant jobs.

Resume:
{resume_text}
"""

    result = agent_executor.invoke({"input": query})

    output = result.get("output", "")

    if isinstance(output, str):
        return output

    if isinstance(output, list):
        return "\n".join(block.get("text", "") for block in output if isinstance(block, dict))

    return str(output)


st.set_page_config(page_title="AI Career Advisor")

st.title("💼 AI Job Recommendation Agent (RAG)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


if uploaded_file is not None:

    resume_text = extract_pdf_text(uploaded_file)

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        response = get_recommendation(resume_text)

        st.subheader("Career Recommendations")

        st.markdown(response)