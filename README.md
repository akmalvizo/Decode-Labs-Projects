# 🚀 Muhammad Akmal — AI Engineering Portfolio
### DecodeLabs Industrial Training Program · Batch 2026

---

## 👤 About Me

**Muhammad Akmal**
AI Engineering Intern · DecodeLabs · Batch 2026

I am an AI engineering intern at DecodeLabs, building real-world artificial intelligence systems through hands-on industrial projects. My training covers the full AI/ML engineering stack — from rule-based systems and classical machine learning to recommendation engines and intelligent application design.

| | |
|---|---|
| 🔗 **LinkedIn** | [LinkedIn](https://www.linkedin.com/in/muhammad-akmal-a329352b0/) |
| 🐙 **GitHub** | [GitHub](https://github.com/akmalvizo) |
| 🌐 **Portfolio** | [Your Live Portfolio URL Here] |
| 📧 **Email** | akmal.vizo@gmail.com |

---

## 🏢 About DecodeLabs

DecodeLabs is a technology training company focused on building real-world AI engineering skills through hands-on industrial projects.

🌐 [www.decodelabs.tech](http://www.decodelabs.tech) · 📧 decodelabs.tech@gmail.com

---

## 📋 Training Program Overview

| Detail | Info |
|---|---|
| **Program** | DecodeLabs Industrial Training Kit |
| **Batch** | 2026 |
| **Track** | Artificial Intelligence |
| **Projects Completed** | 3 of the Industrial Training Kit |
| **Focus Areas** | Rule-Based AI, Supervised ML, Recommendation Systems |

---

## 🗂️ Projects at a Glance

| # | Project | Core Tech | Category |
|---|---------|-----------|----------|
| 1 | [Vizo AI — Rule-Based Chatbot](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/1project) | Python, Control Flow, Dictionaries | Conversational AI |
| 2 | [Iris Flower Classification (KNN)](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/2project) | Scikit-learn, Pandas, Matplotlib | Supervised ML |
| 3 | [Tech Stack Recommender](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/3project) | TF-IDF, Cosine Similarity, Scikit-learn | Recommendation Engine |

---

---

## 🤖 Project 1 · Vizo AI — Rule-Based Chatbot

> 🔗 **GitHub Repository:** [Link](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/1project)

### Overview

**Vizo AI** is a rule-based conversational chatbot built entirely in Python using pure control flow logic — no machine learning, no external AI APIs, no third-party NLP libraries. It simulates human-like conversation by matching user input against a structured knowledge base of keywords and returning context-aware responses.

### Goals & Status

| Goal | Status |
|------|--------|
| Continuous input loop using `while True` | ✅ Complete |
| Input sanitization (case + whitespace) | ✅ Complete |
| Knowledge base with 5+ intent categories | ✅ Complete (17 categories) |
| Keyword-based intent matching engine | ✅ Complete |
| Fallback response for unknown inputs | ✅ Complete |
| Clean exit strategy with kill command | ✅ Complete |
| Dynamic real-time responses (clock) | ✅ Complete |

### Architecture

Vizo AI follows the **IPO Model** (Input → Process → Output):

```
┌─────────────────────────────────────────────────────┐
│                    VIZO AI ENGINE                    │
│                                                      │
│  ┌──────────┐    ┌──────────────┐    ┌───────────┐  │
│  │  INPUT   │───▶│   PROCESS    │───▶│  OUTPUT   │  │
│  │ raw text │    │ sanitize()   │    │ print     │  │
│  │ from     │    │ match_intent │    │ reply to  │  │
│  │ user     │    │ get_response │    │ console   │  │
│  └──────────┘    └──────────────┘    └───────────┘  │
│                                                      │
│  Sanitization ──▶ Intent Matching ──▶ Response Gen   │
└─────────────────────────────────────────────────────┘
```

**Why Dictionary over If-Elif Ladder?**

| Approach | Time Complexity | Scalability | Maintainability |
|----------|----------------|-------------|-----------------|
| If-Elif chain | O(n) — linear | Poor | High technical debt |
| Dictionary `.get()` | O(1) — constant | Excellent | Clean and modular |

### Features

- **17 Intent Categories** with 200+ trigger keywords
- **Keyword-in-sentence matching** — understands phrases, not just exact words
- **Randomized responses** — multiple replies per intent
- **Real-time clock** — dynamically returns current time and date
- **Graceful exit** — handles `quit`, `exit`, `stop`, `end`, `q`, `Ctrl+C`, and `EOF`
- **Zero dependencies** — runs on any machine with Python 3 installed

### Intent Categories

| # | Category | Example Triggers |
|---|----------|-----------------|
| 1 | Greetings | hello, hi, hey, good morning |
| 2 | How Are You | how are you, you doing, you alright |
| 3 | Identity | who are you, what is your name |
| 4 | Location | where are you, where are you going |
| 5 | Current Activity | what are you doing, are you busy |
| 6 | Future Plans | what is your plan, any suggestions |
| 7 | Food & Eating | what should i eat, hungry |
| 8 | Weather | weather today, is it raining |
| 9 | Time & Date | what time is it, today's date |
| 10 | Jokes | tell me a joke, make me laugh |
| 11 | Help | help, what can you do |
| 12 | Feelings & Mood | i am sad, feeling bored |
| 13 | Motivation | motivate me, i want to give up |
| 14 | Study & Learning | how to learn python, coding help |
| 15 | Thanks | thank you, great job |
| 16 | Farewell | bye, goodbye, see you |
| 17 | About AI | what is ai, what is machine learning |

### How the Matching Engine Works

```python
# Step 1: Sanitize — normalize case and remove spaces
clean = raw.lower().strip()        # "  HELLO there  " → "hello there"

# Step 2: Match intent — scan every keyword list
for intent, data in knowledge_base.items():
    for keyword in data["keywords"]:
        if keyword in clean:       # substring match, not exact match
            return intent

# Step 3: Get response — pick randomly from matched intent
reply = random.choice(responses)   # never same reply twice in a row
```

### Sample Interaction

```
You: hello
Vizo: Hey! Great to have you here. What's on your mind?

You: what should i eat today
Vizo: How about biryani? A classic choice for any time of day!

You: tell me a joke
Vizo: Why do programmers prefer dark mode? Because light attracts bugs!

You: i am sad
Vizo: I hear you! Feelings are valid. Take a deep breath -- this too shall pass.

You: bye
Vizo: Goodbye! Keep coding and stay curious!
```

### Getting Started

```bash
git clone [your-project-1-github-link]
cd vizo-ai-chatbot
python chatbot.py
```

### Core Concepts Demonstrated

```
Control Flow     →  while True loop with break condition
Data Structures  →  Dictionary (Hash Map) for O(1) intent lookup
String Methods   →  .lower(), .strip(), in operator
Randomization    →  random.choice() for natural varied responses
Date & Time      →  datetime module for live clock responses
Exception Handling → try/except for KeyboardInterrupt and EOFError
```

---

---

## 🌸 Project 2 · Iris Flower Classification Using KNN

> 🔗 **GitHub Repository:** [link](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/2project)

### Overview

A complete **Supervised Machine Learning pipeline** built from scratch using Python and Scikit-learn. Classifies Iris flowers into *Setosa*, *Versicolor*, or *Virginica* based on physical measurements using the **K-Nearest Neighbors (KNN)** algorithm.

### Concepts Covered

| Concept | Description |
|---|---|
| **Supervised Learning** | Training on labeled examples to predict unseen data |
| **Iris Dataset** | 150 samples, 3 classes, 4 features — the ML benchmark |
| **Feature Scaling** | Normalizing features for fair distance calculations |
| **Train-Test Split** | 80% training / 20% testing with shuffle |
| **KNN Algorithm** | Classifies by majority vote among K nearest points |
| **Elbow Method** | Finds the optimal K value with lowest error rate |
| **Confusion Matrix** | Visual breakdown of correct/incorrect predictions |
| **F1 Score** | Harmonic mean of Precision and Recall |

### Dataset

| Property | Value |
|---|---|
| Total Samples | 150 (Balanced) |
| Classes | 3 (Setosa, Versicolor, Virginica) |
| Features | 4 (Sepal Length, Sepal Width, Petal Length, Petal Width) |
| Missing Values | None |
| Source | `sklearn.datasets.load_iris()` |

### Tech Stack

- **Language:** Python 3.x
- **Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Environment:** Google Colab / Jupyter Notebook

### Pipeline Walkthrough

**Step 1 — Load & Explore**
```python
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
```

**Step 2 — Feature Scaling**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**Step 3 — Train-Test Split**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, shuffle=True
)
```

**Step 4 — Train KNN Model**
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
```

**Step 5 — Elbow Method (Find Optimal K)**
```python
error_rates = []
for k in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(preds != y_test))
best_k = error_rates.index(min(error_rates)) + 1
```

**Step 6 — Evaluate**
```python
f1 = f1_score(y_test, predictions, average='weighted')
# Confusion Matrix plotted via seaborn heatmap
```

**Step 7 — Predict New Data**
```python
new_flower = [[5.1, 3.5, 1.4, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)
```

### Results

| Metric | Value |
|---|---|
| **Optimal K** | Found via Elbow Method |
| **F1 Score (Weighted)** | ~0.97+ |
| **Test Accuracy** | ~95–100% |

### Key Learnings

- Raw accuracy can be misleading on imbalanced datasets — F1 Score is more trustworthy
- Feature Scaling is critical for distance-based algorithms like KNN
- The Elbow Method prevents both overfitting (K=1) and underfitting (K=100)
- Confusion Matrix reveals exactly which classes are being confused

### Getting Started

```bash
git clone [your-project-2-github-link]
cd iris-knn-classification
pip install scikit-learn pandas numpy matplotlib seaborn
# Open iris_classification.ipynb in Google Colab
```

---

---

## 🚀 Project 3 · Tech Stack Recommender

> 🔗 **GitHub Repository:** [link](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/3project)

### Overview

A **content-based AI recommendation engine** that maps a user's raw skills and career goals to the most relevant job roles using TF-IDF weighting and Cosine Similarity. Returns the **Top 3 most relevant career path matches** with percentage scores.

### Core Concepts

**1. Content-Based Filtering**

| Approach | How it works | Used |
|---|---|---|
| Collaborative Filtering | "Users who liked X also liked Y" | ❌ No |
| Content-Based Filtering | Matches user profile to item attributes | ✅ Yes |

**2. Vector Mapping**

Skills are converted into numerical arrays inside a shared vocabulary space:
```
["Python", "Cloud", "Automation"]  →  Vector Mapping  →  [1, 0, 1, 0, 1 ...]
```

**3. TF-IDF Weighting**

```
TF  =  Count of skill in role / Total skills in role
IDF =  log(Total roles / Roles containing that skill)
TF-IDF Score = TF × IDF
```
Result: specific skills like "TensorFlow" carry more weight than generic ones like "Git".

**4. Cosine Similarity**

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

| Score | Meaning |
|---|---|
| 1.0 | Perfect match |
| 0.5–0.9 | Strong match |
| 0.1–0.4 | Partial match |
| 0.0 | No overlap |

**5. The 4-Step Ranking Pipeline**

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  STEP 1     │────▶│  STEP 2     │────▶│  STEP 3     │────▶│  STEP 4     │
│  Ingestion  │     │  Scoring    │     │  Sorting    │     │  Filtering  │
│ Capture     │     │ Cosine      │     │ Sort by     │     │ Return      │
│ user skills │     │ Similarity  │     │ score desc  │     │ Top 3 list  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### Dataset — Job Roles Covered

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

### Sample Output

```
==================================================
   Top 3 Recommended Career Paths For You
==================================================

#1 ML Engineer
   Match Score : 71.3%
   Key Skills  : Python, TensorFlow, Machine Learning, Deep Learning

#2 Data Scientist
   Match Score : 65.8%
   Key Skills  : Python, SQL, Machine Learning, Statistics, TensorFlow

#3 AI Research Scientist
   Match Score : 44.2%
   Key Skills  : Python, Research, Deep Learning, NLP, Mathematics
==================================================
```

### Test Cases

| Input Skills | Expected Top Match |
|---|---|
| `Python, Machine Learning, TensorFlow` | ML Engineer / Data Scientist |
| `AWS, Docker, Automation` | DevOps Engineer / Cloud Architect |
| `JavaScript, React, HTML` | Frontend Developer |
| `SQL, Excel, Data Analysis` | Data Analyst |
| `Networking, Security, Linux` | Cybersecurity Engineer |

### Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset loading and manipulation |
| Scikit-Learn TfidfVectorizer | TF-IDF feature extraction |
| Scikit-Learn cosine_similarity | Similarity scoring |
| CSV | Lightweight job role dataset |

### Getting Started

```bash
git clone [your-project-3-github-link]
cd tech-stack-recommender
pip install scikit-learn pandas
python recommender.py
```

---

---

## 📈 Skills Progression Across Projects

| Skill Area | Project 1 | Project 2 | Project 3 |
|---|---|---|---|
| Python Fundamentals | ✅ Core | ✅ Applied | ✅ Applied |
| Data Structures | ✅ Dictionaries | ✅ DataFrames | ✅ Vectors |
| Machine Learning | ❌ Rule-based | ✅ KNN | ✅ TF-IDF |
| Algorithm Design | ✅ O(1) lookup | ✅ Elbow Method | ✅ Cosine Similarity |
| Evaluation Metrics | ❌ | ✅ F1, Confusion Matrix | ✅ Similarity Score |
| Libraries Used | Standard Library only | scikit-learn, pandas | scikit-learn, pandas |
| AI Type | Deterministic / White Box | Probabilistic / Supervised | Content-Based / Unsupervised |

---

## 🔮 Future Roadmap

- Expand Vizo AI with conversation memory and a Flask web frontend
- Benchmark KNN against Decision Trees, SVM, and Logistic Regression
- Grow the Tech Stack Recommender to 50+ job roles with hybrid filtering
- Deploy all three projects as live web applications
- Implement cross-validation for more robust ML evaluation

---

## 📄 License

All projects were created as part of the **DecodeLabs Industrial Training Program**.
© 2026 Muhammad Akmal · DecodeLabs Batch 2026

---

<p align="center">
  Built with 💚 during the DecodeLabs AI Industrial Training Program<br>
  <em>"An LLM without rules is a hallucination engine. This project builds the skeleton that holds the intelligence." — DecodeLabs</em>
</p>
