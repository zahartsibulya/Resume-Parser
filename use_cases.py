# use_cases.py
from domain import JOB_REQUIREMENTS

def evaluate_candidate(candidate_dto: dict) -> dict:
    """Головний Use Case: оцінює DTO кандидата відносно вимог"""
    score = 0
    candidate_exp = candidate_dto.get("years_of_experience")
    
    if isinstance(candidate_exp, (int, float)):               #оцінюємо досвід
        if candidate_exp >= JOB_REQUIREMENTS["min_experience"]:
            score += 40
        elif candidate_exp > 0:
            score += 20

    candidate_skills = [s.lower() for s in candidate_dto.get("core_skills", [])]#оцінюємо навички
    required_skills = [s.lower() for s in JOB_REQUIREMENTS["required_skills"]]
    
    matched_skills = 0
    for req_skill in required_skills:
        if any(req_skill in c_skill for c_skill in candidate_skills):
            matched_skills += 1
            
    if required_skills:
        skills_score = (matched_skills / len(required_skills)) * 60
        score += int(skills_score)
        
    status = "Approved" if score >= 70 else "Rejected"
    

    return {                  #повертаємо вихідний DTO
        "status": status,
        "match_score": score,
        "matched_skills_count": matched_skills,
        "total_required_skills": len(required_skills),
        "candidate_details": candidate_dto
    }
