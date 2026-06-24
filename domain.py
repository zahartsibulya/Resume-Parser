# domain.py

JOB_REQUIREMENTS = {
    "min_experience": 2,
    "required_skills": ["Python", "Flask", "Docker", "SQL", "Git"]
}

# Системний промпт також є частиною бізнес-правил екстракції
SYSTEM_PROMPT = """
Ти — професійний HR-асистент. Витягни дані з резюме та ПОВИНЕН повернути валідний JSON:
{
    "name": "Ім'я (або null)",
    "years_of_experience": Досвід у роках (ціле число),
    "core_skills": ["навичка 1", "навичка 2", "навичка 3" (і т.д.)],
    "english_level": "Рівень (або null)"
}
"""