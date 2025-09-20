# 🚀 Startup Hiring Assistant

A full-stack Python prototype to help early-stage startups **filter, rank, and select top candidates** from LinkedIn/form submissions based on job description similarity.

---

## 📋 Overview

After raising a seed round, you have hundreds of applicants but only a team of one. This tool allows you to:

* Filter candidates by **job title**
* Rank candidates based on **semantic similarity** between the job description and candidate submissions
* Quickly select a **diverse top 5** candidates to hire with reasoning
* Visualize and interact with candidate data in a simple web interface

This prototype is designed for **quick demo purposes**, but can be extended to a production-grade hiring platform.

---

## ⚡ Features

* Input a **job title** and **job description**
* Filter candidates by **job title**
* Rank candidates by **similarity score** (based on resume or submitted text)
* Display **top 5 recommended hires** with selection reasoning
* Interactive **Streamlit interface** for easy use

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Streamlit** – frontend interface
* **pandas** – data manipulation
* **sentence-transformers** – semantic embeddings & similarity scoring
* **scikit-learn** – optional for additional ranking or filtering

---

## 🚀 Setup & Run

1. Clone this repository:

```bash
git clone https://github.com/Ayoub-etoullali/AI-Powered-Candidate-Ranking-Hiring-Assistant
cd AI-Powered-Candidate-Ranking-Hiring-Assistant
```

2. Install dependencies:

```bash
pip install streamlit pandas sentence-transformers sklearn
```

3. Place your candidate data JSON file (`form-submissions.json`) in the project folder.

4. Run the app:

```bash
streamlit run app.py
```

5. Open the browser interface and enter the **job title** and **job description** to see top candidate recommendations.

---

## 📝 Usage

1. Enter a **Job Title** (optional) to filter candidates.
2. Enter the **Job Description** of the role you’re hiring for.
3. The app computes similarity scores between the job description and candidate responses.
4. Top candidates are displayed with scores and reasoning.
5. Select your **top 5 hires** for demo or decision-making.

---

## 📈 Future Enhancements

* Include **diversity filters** (location, experience, skills)
* Visualize candidate **skills vs. job requirements**
* Auto-generate **email templates** for shortlisted candidates
* Integrate with **LinkedIn / ATS APIs** for live updates
* Use **OpenAI embeddings** for higher semantic accuracy

---

## 📄 License

This project is open-source and free to use for **demonstration and prototyping purposes**.
