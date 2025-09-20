import streamlit as st
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

# -------------------------------
# Load candidate data
# -------------------------------
with open("data/form-submissions.json") as f:
    candidates = json.load(f)

# -------------------------------
# App UI
# -------------------------------
st.title("🚀 Startup Hiring Assistant")
st.write("Filter candidates by job title and match them to your ideal job description.")

# Input job title & description
job_title = st.text_input("Enter Job Title", "")
job_description = st.text_area("Enter Job Description", "")

# Filter candidates by job title if provided
# if job_title:
#     filtered_df = df[df['job_title'].str.contains(job_title, case=False, na=False)]
# else:
#     filtered_df = df.copy()
filtered_df = filter_by_job_title(candidates, job_title)
df = pd.DataFrame(filtered_df)

st.write(f"Found {len(filtered_df)} candidates matching the job title.")

# -------------------------------
# Compute similarity
# -------------------------------
if job_description and len(filtered_df) > 0:
    st.write("Calculating similarity scores...")
    
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Embed job description
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    
    # Embed candidate answers (assuming a 'resume_text' field)
    candidate_embeddings = model.encode(filtered_df['resume_text'].tolist(), convert_to_tensor=True)
    
    # Compute cosine similarity
    similarity_scores = util.cos_sim(job_embedding, candidate_embeddings)[0].tolist()
    
    filtered_df['similarity_score'] = similarity_scores
    
    # Sort candidates by similarity
    filtered_df = filtered_df.sort_values(by='similarity_score', ascending=False)
    
    st.write("Top candidates:")
    st.dataframe(filtered_df[['name', 'job_title', 'similarity_score']].head(10))
    
    # -------------------------------
    # Pick top 5 candidates for demo
    # -------------------------------
    top5 = filtered_df.head(5)
    
    st.write("✅ Recommended 5 candidates to hire:")
    for idx, row in top5.iterrows():
        st.write(f"**{row['name']}** ({row['job_title']}) — Similarity Score: {row['similarity_score']:.2f}")
        st.write(f"Reason for selection: High similarity to job description and relevant experience.")
        st.markdown("---")
else:
    st.info("Enter a job description to rank candidates.")
