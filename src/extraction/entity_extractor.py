import re


def extract_entities(text: str):
    """
    Simple rule-based entity extraction from resume / JD text.
    """

    entities = {
        "name": None,
        "role": None,
        "skills": [],
        "experience": None
    }

    # Extract name
    name_match = re.search(r"Name:\s*(.*)", text)
    if name_match:
        entities["name"] = name_match.group(1).strip()

    # Extract role
    role_match = re.search(r"Role:\s*(.*)", text)
    if role_match:
        entities["role"] = role_match.group(1).strip()

    # Extract experience
    exp_match = re.search(r"Experience:\s*(.*)", text)
    if exp_match:
        entities["experience"] = exp_match.group(1).strip()

    # Extract skills
    skills_match = re.search(r"Skills:\s*([\s\S]*?)\n\n", text)
    if skills_match:
        skills_text = skills_match.group(1)
        skills = [skill.strip() for skill in skills_text.split(",")]
        entities["skills"] = skills

    return entities
