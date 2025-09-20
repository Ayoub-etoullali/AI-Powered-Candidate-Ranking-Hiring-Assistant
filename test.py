import pandas as pd

def filter_by_job_title(candidates, job_title):
    """
    Filters candidates by job title, checking across all work_experiences.roleName.
    """
    if not job_title:
        return candidates  # no filtering
    
    filtered = []
    for candidate in candidates:
        experiences = candidate.get("work_experiences", [])
        # check if any past role contains the job title
        if any(job_title.lower() in exp["roleName"].lower() for exp in experiences):
            filtered.append(candidate)
    return filtered

# Example usage
import json

with open("data/form-submissions.json") as f:
    candidates = json.load(f)

filtered_candidates = filter_by_job_title(candidates, "Data Science")
df = pd.DataFrame(filtered_candidates)
print(df)