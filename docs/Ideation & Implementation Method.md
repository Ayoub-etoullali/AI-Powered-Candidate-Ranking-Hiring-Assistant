## 💡 Ideation & Implementation Method

### 1. Problem Understanding

The challenge was to quickly process **hundreds of candidate submissions** and select a **diverse team of 5 hires** that best match a role.
Key needs identified:

* Avoid manual screening → **automated filtering & ranking**
* Capture semantic meaning → not just keyword matching, but **understanding resumes vs. job descriptions**
* Provide a **clear and intuitive interface** for decision-making

---

### 2. Approach & Design Choices

* **Input-driven filtering**:
  The user inputs a **Job Title** → filters candidates early to reduce noise and complexity.

* **Similarity-based ranking**:
  Instead of raw keyword search, I used **semantic embeddings (Sentence Transformers)** to compute how closely a candidate’s submission matches the provided **job description**.

  * This ensures candidates are ranked by **meaning**, not just overlapping words.

* **Top 5 Recommendations**:
  The app automatically recommends **five hires** with highest similarity scores. Each candidate is displayed with:

  * Name
  * Job Title
  * Similarity Score
  * Selection Reason

* **Simple UX with Streamlit**:

  * Fast to build, deploy, and demo
  * Interactive data filtering and ranking visualization
  * Minimal learning curve for non-technical users

---

### 3. Implementation Steps

1. **Data Ingestion**:
   Loaded JSON form submissions into a `pandas` DataFrame.

2. **Filtering**:
   Applied job-title filtering (`contains` match) to narrow down candidates.

3. **Embedding & Similarity**:

   * Encoded job description and candidate resume text using **all-MiniLM-L6-v2** model (Sentence Transformers).
   * Computed **cosine similarity** between embeddings.
   * Assigned similarity scores to each candidate.

4. **Ranking & Selection**:

   * Sorted candidates by similarity (descending).
   * Extracted **Top 5** as recommended hires.

5. **Frontend/UI**:

   * Built with **Streamlit** for instant interactivity.
   * Displayed filtered candidate lists, similarity scores, and recommendations.

---

### 4. Why This Approach Works

* **Scalable**: Can handle hundreds of candidates without manual review.
* **Flexible**: Any job description can be input and evaluated instantly.
* **Transparent**: Provides reasoning for each selection (score + description).
* **Extendable**: Can add diversity filters, visualization, or ATS integration in the future.
