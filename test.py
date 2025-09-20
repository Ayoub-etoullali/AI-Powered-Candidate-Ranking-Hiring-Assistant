import pandas as pd
from sentence_transformers import SentenceTransformer, util
import json

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

def build_profile_text(candidate):
    """Concatenate work experiences, skills, and education into one text string."""
    experiences = " ".join([exp["roleName"] for exp in candidate.get("work_experiences", [])])
    skills = " ".join(candidate.get("skills", []))
    education = " ".join([deg.get("subject", "") for deg in candidate.get("education", {}).get("degrees", [])])
    
    return f"{experiences} {skills} {education}"

# -------------------------------
# Load candidate data
# -------------------------------
with open("data/form-submissions.json") as f:
    candidates = json.load(f)

# -------------------------------
# App UI
# -------------------------------

# Input job title & description
job_title ="Data Scientist"
job_description = """
Collecter, nettoyer et structurer les données provenant des systèmes avion et des opérations aériennes.
"""

# Filter candidates by job title if provided
# Filter candidates by job title if provided
filtered_candidates = filter_by_job_title(candidates, job_title)

df_candidates = pd.DataFrame(filtered_candidates)

print(f"Found {len(filtered_candidates)} candidates matching the job title.")

# -------------------------------
# Compute similarity
# -------------------------------
if job_description and len(filtered_candidates) > 0:
    print("Calculating similarity scores...")
    
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Build profile text
    def build_profile_text(row):
        experiences = " ".join([exp["roleName"] for exp in row.get("work_experiences", [])])
        skills = " ".join(row.get("skills", []))
        education = " ".join([deg.get("subject", "") for deg in row.get("education", {}).get("degrees", [])])
        return f"{experiences} {skills} {education}"

    # Apply row-wise
    df_candidates["profile_text"] = df_candidates.apply(build_profile_text, axis=1)

    # Encode job description
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    # Encode candidate profiles
    candidate_embeddings = model.encode(df_candidates["profile_text"].tolist(), convert_to_tensor=True)

    # Compute cosine similarity
    similarity_scores = util.cos_sim(job_embedding, candidate_embeddings)[0].tolist()
    df_candidates["similarity_score"] = similarity_scores

    # Pick a display job title (first role)
    df_candidates["display_job_title"] = df_candidates["work_experiences"].apply(
        lambda exps: exps[0]["roleName"] if exps else "N/A"
    )

    # Sort by similarity
    df_candidates = df_candidates.sort_values(by="similarity_score", ascending=False)

    # Show top candidates
    print("### Top candidates:")
    print(df_candidates[["name", "display_job_title", "similarity_score"]].head(10))

    # -------------------------------
    # Pick top 5 candidates
    # -------------------------------
    print("### ✅ Recommended 5 candidates to hire:")
    top5 = df_candidates.head(5)

    for idx, row in top5.iterrows():
        print(f"**{row['name']}** ({row['display_job_title']}) — "
                 f"Similarity Score: {row['similarity_score']:.2f}")
        print("Reason for selection: High similarity to job description and relevant experience.")
        print("---")

else:
    print("Enter a job description to rank candidates.")