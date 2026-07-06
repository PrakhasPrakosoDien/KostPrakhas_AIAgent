import google.generativeai as genai

from config import *
from prompt import SYSTEM_PROMPT
from knowledge import load_knowledge

genai.configure(api_key=GEMINI_API_KEY)

model=genai.GenerativeModel(MODEL_NAME)

knowledge=load_knowledge()

def ask_gemini(question):

    prompt=f"""
{SYSTEM_PROMPT}

Data Kos:

{knowledge}

Pertanyaan User:

{question}

Jawaban:
"""

    response=model.generate_content(prompt)

    return response.text
