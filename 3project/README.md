# 🚀 Tech Stack Recommender
### AI Recommendation Logic — Project 3 | DecodeLabs Industrial Training Kit | Batch 2026

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data-green?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

The **Tech Stack Recommender** is a content-based AI recommendation engine built as part of the **DecodeLabs Industrial Training Program (Batch 2026)**. This project represents the transition from passive data classification to **active prediction** — mapping a user's raw skills and career goals to the most relevant job roles using pure algorithmic similarity logic.

Instead of random suggestions, this system uses **Pattern Alignment**: it mathematically measures how closely a user's skill set aligns with the requirements of various tech career paths and returns the **Top 3 most relevant matches**.

---

## 🎯 Project Goal

> Build a simple yet powerful recommendation system that takes user skill inputs, matches them to job roles using TF-IDF weighting and Cosine Similarity, and displays ranked career path recommendations.

---

## 🧠 Core Concepts Used

### 1. Content-Based Filtering
Unlike collaborative filtering (which needs massive historical user datasets), content-based filtering works by mapping a user's profile **directly to item attributes** — in this case, matching user skills to job role skill requirements. This approach works immediately without needing other users' data.

| Approach | How it works | Used in this project |
|---|---|---|
| Collaborative Filtering | "Users who liked X also liked Y" | ❌ No |
| Content-Based Filtering | Matches user profile to item attributes | ✅ Yes |

---

### 2. Vector Mapping
Machines cannot understand words like "Python" or "Cloud Computing". Every skill tag is converted into a **numerical array (vector)** inside a shared vocabulary space. If a user selects "Java" and "SQL", those dimensions in the mathematical space are activated.

```
["Python", "Cloud", "Automation"]  →  Vector Mapping  →  [1, 0, 1, 0, 1 ...]
```

> ⚠️ Item features and user features must map to the **exact same vocabulary**. Naming discrepancies (e.g., "Web Design" vs "Frontend Development") will cause the similarity math to fail.

---

### 3. TF-IDF Weighting (Term Frequency — Inverse Document Frequency)
Simple binary matching (0 or 1) treats every skill equally. TF-IDF solves this by:

- **Term Frequency (TF):** Rewards skills that appear frequently within a specific job role
- **Inverse Document Frequency (IDF):** Penalizes generic skills that appear across all roles (like "Git" or "Python")

The result: **specific, rare skills like "TensorFlow" carry more weight than common ones**, producing more accurate recommendations.

```
TF  =  Count of skill in role / Total skills in role
IDF =  log(Total roles / Roles containing that skill)
TF-IDF Score = TF × IDF
```

---

### 4. Cosine Similarity (The Core Engine)
After vectorizing, the system measures the **angular closeness** between the user profile vector and each job role vector.

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

| Score | Meaning |
|---|---|
| 1.0 | Perfect match — identical orientation |
| 0.5–0.9 | Strong match |
| 0.1–0.4 | Partial match |
| 0.0 | No overlap at all |

> Cosine Similarity is preferred over Euclidean Distance because it is **magnitude-invariant** — it focuses on the direction of preferences, not the size of the feature set. This prevents longer job descriptions from unfairly dominating results.

---

### 5. The 4-Step Ranking Pipeline

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  STEP 1     │────▶│  STEP 2     │────▶│  STEP 3     │────▶│  STEP 4     │
│  Ingestion  │     │  Scoring    │     │  Sorting    │     │  Filtering  │
│             │     │             │     │             │     │             │
│ Capture     │     │ Calculate   │     │ Sort by     │     │ Return      │
│ user skills │     │ Cosine      │     │ score       │     │ Top-N list  │
│ (min 3)     │     │ Similarity  │     │ descending  │     │ (Top 3)     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## 📁 Project Structure

```
3project/
│
├── recommender.py       # Main Python script (recommendation engine)
├── raw_skills.csv       # Dataset of job roles and their required skills
└── README.md            # Project documentation (this file)
```

---

## 📊 Dataset — `raw_skills.csv`

The dataset treats each **job role as an "item"** in the recommendation engine. Each role has a curated list of skills that define it.

| Job Role | Key Skills |
|---|---|
| Data Scientist | Python, SQL, Machine Learning, Statistics, TensorFlow |
| ML Engineer | Python, TensorFlow, Machine Learning, Deep Learning |
| Data Analyst | SQL, Excel, Python, Data Analysis, Visualization |
| Backend Developer | Java, Python, SQL, APIs, Node.js |
| Frontend Developer | JavaScript, HTML, CSS, React, UI/UX |
| Cloud Architect | AWS, Cloud Computing, Automation, Kubernetes |
| DevOps Engineer | AWS, Docker, Kubernetes, CI/CD, Linux |
| Cybersecurity Engineer | Networking, Security, Linux, Ethical Hacking |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.11 or above
- pip package manager

### Step 1 — Clone the Repository
```bash
git clone https://github.com/your-username/tech-stack-recommender.git
cd tech-stack-recommender
```

### Step 2 — Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install scikit-learn pandas
```

### Step 4 — Run the Project
```bash
python recommender.py
```

---

## 💻 How to Use

1. Run the script
2. Enter **at least 3 skills** separated by commas when prompted
3. The system returns your **Top 3 matched career paths** with similarity scores
4. Enter new skills to try again.

```
==================================================
   Welcome to the Tech Stack Recommender
==================================================

Enter at least 3 skills (comma-separated).
Example: Python, SQL, Machine Learning

Your skills: Python, Machine Learning, TensorFlow

==================================================
   Top 3 Recommended Career Paths For You
==================================================

#1 ML Engineer
   Match Score : 71.3%
   Key Skills  : Python, TensorFlow, Machine Learning, Deep Learning, Data Analysis, Git

#2 Data Scientist
   Match Score : 65.8%
   Key Skills  : Python, SQL, Machine Learning, Statistics, Data Analysis, TensorFlow

#3 AI Research Scientist
   Match Score : 44.2%
   Key Skills  : Python, Research, Deep Learning, NLP, Mathematics, TensorFlow

==================================================
Recommendation complete. Good luck!
==================================================
```

---

## 🧪 Test Cases

| Input Skills | Expected Top Match |
|---|---|
| `Python, Machine Learning, TensorFlow` | ML Engineer / Data Scientist |
| `AWS, Docker, Automation` | DevOps Engineer / Cloud Architect |
| `JavaScript, React, HTML` | Frontend Developer |
| `Java, Python, SQL` | Backend Developer |
| `Networking, Security, Linux` | Cybersecurity Engineer |
| `SQL, Excel, Data Analysis` | Data Analyst |

---

## 🔍 The Cold Start Problem

Even the best recommendation engine fails without initial data. This project addresses the **Cold Start problem** in two ways:

- **User Cold Start** → Solved by requiring a **minimum of 3 skill inputs** (onboarding survey approach), forcing enough data density for accurate vector matching
- **Item Cold Start** → Content-based filtering is naturally immune — new job roles can be recommended immediately once their skill tags are added to the dataset

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset loading and manipulation |
| Scikit-Learn (TfidfVectorizer) | TF-IDF feature extraction |
| Scikit-Learn (cosine_similarity) | Similarity scoring |
| CSV | Lightweight job role dataset |

---

## 🔮 Future Improvements

- [ ] Add a GUI interface using Tkinter or Streamlit
- [ ] Expand dataset to 50+ job roles
- [ ] Add user rating system for feedback loop
- [ ] Implement hybrid filtering (content + collaborative)
- [ ] Export recommendations as PDF report
- [ ] Deploy as a web application

---

## 👨‍💻 Author

**Built by "Muhammad Akmal" during Industrial Training at DecodeLabs**
- Batch: 2026
- Track: Artificial Intelligence
- Project: 3 — AI Recommendation Logic
- Company: [DecodeLabs](https://www.decodelabs.tech)

---

## 📄 License

This project is built for educational purposes as part of the DecodeLabs Industrial Training Program.

---

> *"The absolute best way to master Artificial Intelligence is through hands-on practice, not just theory."*
> — DecodeLabs