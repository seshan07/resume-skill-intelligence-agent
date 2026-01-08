import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # LLM configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL")

    # API configuration
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))

    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    RESUME_DIR = os.path.join(DATA_DIR, "resumes")
    JD_DIR = os.path.join(DATA_DIR, "job_descriptions")
