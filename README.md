# 📄 AI Job Recommendation Agent (RAG + LangChain + Gemini)

An **AI-powered career advisor** that analyzes resumes and recommends suitable job roles and companies using **Retrieval-Augmented Generation (RAG)**, **LangChain agents**, and **Google Gemini**.

The system extracts information from a resume, retrieves relevant jobs from a knowledge base using **vector search**, and suggests companies hiring for those roles.

---

# 🚀 Features

- 📄 **PDF Resume Upload**
- 🧠 **Automatic Skill Extraction**
- 💼 **Job Role Recommendation**
- 🏢 **Company Suggestions**
- 🔎 **RAG-based Job Retrieval**
- 🤖 **LangChain Tool-Calling Agent**
- ⚡ **Gemini LLM Integration**
- 🖥 **Interactive Streamlit UI**

---

# 🧠 Architecture


Resume PDF
│
▼
Text Extraction
│
▼
Embedding Model (Gemini Embeddings)
│
▼
Vector Database (FAISS)
│
Retrieve Relevant Jobs
│
▼
LangChain Agent
│
▼
Gemini LLM
│
▼
Recommended Jobs + Companies


---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| LangChain | Agent + tool orchestration |
| Google Gemini API | LLM reasoning |
| FAISS | Vector database for RAG |
| Google Embeddings | Text embeddings |
| Streamlit | Web UI |
| PyPDF2 | Resume parsing |

---

# 📂 Project Structure


job-ai-agent/

app.py
tools.py
rag.py

data/
jobs.txt
companies.csv

requirements.txt
README.md


---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/job-ai-agent.git
cd job-ai-agent
2️⃣ Create virtual environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
🔑 Setup API Key

Create a .env file in the project root:

GOOGLE_API_KEY=your_gemini_api_key

You can get your API key from:

https://ai.google.dev

▶️ Run the Application
streamlit run app.py

The app will open in your browser:

http://localhost:8501
💡 Example Workflow

Upload a PDF resume

The system extracts resume text

Skills are identified

Relevant jobs are retrieved using RAG

Gemini analyzes the results

The agent returns:

Recommended job roles

Companies hiring for those roles

Example output:

Detected Skills:
Python, Machine Learning, NLP

Recommended Roles:
Machine Learning Engineer
AI Engineer
Data Scientist

Top Companies Hiring:
Google, Microsoft, Amazon
📊 Example Queries

You can ask the agent:

Analyze my resume and suggest jobs
What roles match this resume?
Which companies hire for these roles?
🔍 Key AI Concepts Demonstrated

This project showcases:

Retrieval-Augmented Generation (RAG)

LangChain tool-calling agents

Vector databases

LLM-powered applications

AI career recommendation systems

📈 Why This Project Matters

This project demonstrates real-world Generative AI system design, including:

LLM integration

knowledge retrieval

AI agents

vector search

resume analysis

These are common patterns used in modern AI products and startups.

🧑‍💻 Future Improvements

Possible enhancements:

ATS resume scoring

Interview question generator

LinkedIn job scraping

Multi-agent architecture

Resume skill gap analysis

📜 License

This project is open-source and available under the MIT License.
