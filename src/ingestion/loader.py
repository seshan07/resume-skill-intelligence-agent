import os
from src.config import Config


def load_text_files(folder_path: str):
    documents = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            documents.append({
                "file_name": file_name,
                "content": text
            })

    return documents


def load_resumes():
    return load_text_files(Config.RESUME_DIR)


def load_job_descriptions():
    return load_text_files(Config.JD_DIR)