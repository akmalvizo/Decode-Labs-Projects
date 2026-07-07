# 🚀 Muhammad Akmal — AI Engineering Portfolio
### DecodeLabs Industrial Training Program · Batch 2026

---

## 👤 About Me

**Muhammad Akmal**
AI Engineering Intern · DecodeLabs · Batch 2026
CS Student (2022–2026) — University of Education, Lahore

I am an AI engineering intern at DecodeLabs, building real-world artificial intelligence systems through hands-on industrial projects. My training covers the full AI/ML engineering stack — from rule-based systems and classical machine learning to recommendation engines, intelligent application design, and machine perception (OCR / image & text recognition).

| | |
|---|---|
| 🔗 **LinkedIn** | [LinkedIn](https://www.linkedin.com/in/muhammad-akmal-a329352b0/) |
| 🐙 **GitHub** | [GitHub](https://github.com/akmalvizo) |
| 🌐 **Portfolio** | [Akmal Portfolio](https://akmal-vizo-portfolio.vercel.app/) |
| 📧 **Email** | akmal.vizo@gmail.com |

[![Portfolio](https://img.shields.io/badge/Portfolio-Live-00C853?style=for-the-badge&logo=vercel&logoColor=white)](https://akmal-vizo-portfolio.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-akmalvizo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/akmalvizo)

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
| **Projects Completed** | 4 of the Industrial Training Kit (3 core + 1 optional mastery phase) |
| **Focus Areas** | Rule-Based AI, Supervised ML, Recommendation Systems, Image & Text Recognition (OCR) |

---

## 🗂️ Projects at a Glance

| # | Project | Core Tech | Category |
|---|---------|-----------|----------|
| 1 | [Vizo AI — Rule-Based Chatbot](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/1project) | Python, Control Flow, Dictionaries | Conversational AI |
| 2 | [Iris Flower Classification (KNN)](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/2project) | Scikit-learn, Pandas, Matplotlib | Supervised ML |
| 3 | [Tech Stack Recommender](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/3project) | TF-IDF, Cosine Similarity, Scikit-learn | Recommendation Engine |
| 4 | [OCR Image & Text Recognition Pipeline](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/4project) | Tesseract, OpenCV, pytesseract | Image & Text Recognition |

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

## 🔍 Project 4 · OCR Image & Text Recognition Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11.0-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-5.5.0-DD0031?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-00C853?style=for-the-badge)
![Internship](https://img.shields.io/badge/DecodeLabs-Project%204-FF6F00?style=for-the-badge)

**Project 4 — Optional Mastery Phase | DecodeLabs AI Engineering Internship — Batch 2026**

*A production-ready OCR pipeline that extracts machine-readable text from raw visual data using pre-trained AI libraries, image pre-processing, and confidence-based filtering.*

</div>

> 🔗 **GitHub Repository:** [Link](https://github.com/akmalvizo/Decode-Labs-Projects/tree/main/4project)

### 📌 Table of Contents

- [Project Overview](#-project-overview-p4)
- [Core Concepts](#-core-concepts-p4)
- [System Architecture](#-system-architecture-p4)
- [Tech Stack & Toolkit](#-tech-stack--toolkit-p4)
- [Pre-Processing Pipeline](#-pre-processing-pipeline-p4)
- [Confidence Filtering](#-confidence-filtering--the-80-threshold)
- [Milestone Validations](#-milestone-validations)
- [Project Structure](#-project-structure-p4)
- [Installation Guide](#-installation-guide-p4)
- [How to Run](#-how-to-run)
- [Sample Output](#-sample-output-p4)
- [PSM Mode Guide](#-psm-mode-guide)
- [Key Learnings](#-key-learnings-p4)
- [About the Internship](#-about-the-internship)

---

### 🧠 Project Overview {#-project-overview-p4}

This project is the **4th and final milestone** of the DecodeLabs AI Engineering Industrial Training Program (Batch 2026). It falls under the **Optional Mastery Phase: Image or Text Recognition (Basic)**.

The goal was to move beyond structured tabular data (previous projects used KNN, TF-IDF, cosine similarity) and enter the domain of **machine perception** — the ability for a computer to read and interpret raw visual data.

#### What It Does

Given any image containing printed text (a document, invoice, screenshot, book page, or sign), this pipeline:

1. **Loads** the raw image into memory as a 3D pixel array
2. **Pre-processes** it through a 5-step cleaning pipeline (grayscale → denoise → contrast → blur → threshold)
3. **Runs OCR** via Google's Tesseract engine (wrapped through pytesseract)
4. **Filters results** — only words scoring **≥ 80% confidence** are accepted
5. **Visualizes output** — draws green bounding boxes around every confirmed word
6. **Exports** three files: the pre-processed image, the annotated output image, and console-printed extracted text

#### Why This Matters

> Over 80% of enterprise data lives in unstructured formats — scanned documents, raw images, video feeds. This project builds the bridge between physical visual data and computational logic.

---

### 📚 Core Concepts {#-core-concepts-p4}

#### 1. How a Machine Sees an Image

A machine does not see a picture. It sees a **3D numerical array** of shape `(Height, Width, Channels)`:

```
Image Shape: (H, W, 3)
             ↑  ↑  ↑
             │  │  └─ 3 Color Channels: Red, Green, Blue
             │  └──── Width in pixels
             └─────── Height in pixels
```

Every single pixel holds 3 values (R, G, B), each ranging from 0–255. A 512×512 image = **786,432 distinct data points**. Modifying a single coordinate directly alters what the machine perceives.

#### 2. Transfer Learning — Why We Don't Train From Scratch

Training an OCR model requires millions of labeled images and weeks of compute time. Instead, this project uses **Transfer Learning**:

- **The Base:** Tesseract's engine was pre-trained on massive text datasets and already understands universal visual patterns (edges, strokes, character contours)
- **The Transfer:** We plug our specific images directly into this pre-trained engine
- **The Advantage:** High-accuracy text recognition using zero training time and minimal compute resources

#### 3. The IPO Model (Input → Process → Output)

```
Raw Image (PNG/JPG)
       ↓
  [Pre-Processing]     ← Grayscale, Denoise, CLAHE, Blur, Threshold
       ↓
  [OCR Engine]         ← Tesseract + pytesseract (convolutional + BiLSTM pipeline)
       ↓
  [Confidence Filter]  ← Keep only words ≥ 80% confidence
       ↓
Extracted Text + Bounding Box Visual Output
```

#### 4. What is OCR?

**Optical Character Recognition (OCR)** is the technology that converts images of text into machine-readable strings. Tesseract internally uses a **Convolutional Neural Network + Bi-directional LSTM pipeline** to read character sequences from images.

It does not "know" what a word is. It calculates the **statistical probability** of what each character sequence most likely represents, then attaches a confidence score to each result.

---

### 🏗 System Architecture {#-system-architecture-p4}

```
┌─────────────────────────────────────────────────────────────────┐
│                        INPUT LAYER                              │
│              sample.png  (any printed text image)               │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PRE-PROCESSING PIPELINE                      │
│                                                                 │
│   Step 1: Grayscale Conversion  → Collapse RGB to 1D intensity  │
│   Step 2: Denoising             → fastNlMeansDenoising (h=10)   │
│   Step 3: CLAHE Contrast        → clipLimit=2.0, tile=(8,8)     │
│   Step 4: Gaussian Blur         → Kernel (3,3) — remove noise   │
│   Step 5: Adaptive Threshold    → Binary black-and-white image  │
│                                                                 │
│   Output: preprocessed.png                                      │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OCR ENGINE LAYER                          │
│                                                                 │
│   Engine  : Google Tesseract v5.5.0 (via pytesseract wrapper)   │
│   Mode    : --oem 3 (LSTM + Legacy) --psm 6 (Uniform text block)│
│   Output  : Per-word data dict (text, confidence, bbox coords)  │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                   CONFIDENCE FILTER LAYER                       │
│                                                                 │
│   Threshold : 80% minimum (project requirement)                 │
│   Logic     : if confidence >= 80 → ACCEPT  else → DROP         │
│   Filter    : Also removes single-character noise symbols       │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OUTPUT LAYER                              │
│                                                                 │
│   1. Console: Word-by-word results with confidence scores       │
│   2. output_result.png: Original image + green bounding boxes   │
│   3. preprocessed.png: Proof of pre-processing pipeline         │
└─────────────────────────────────────────────────────────────────┘
```

---

### 🛠 Tech Stack & Toolkit {#-tech-stack--toolkit-p4}

| Component | Tool | Version | Role |
|-----------|------|---------|------|
| Language | Python | 3.11.0 | Core scripting language |
| OCR Engine | Tesseract | 5.5.0 | Google's open-source OCR engine |
| OCR Wrapper | pytesseract | latest | Python interface for Tesseract |
| Computer Vision | OpenCV (cv2) | 4.13.0 | Image loading, processing, drawing |
| Image Handling | Pillow | latest | PIL image format support |
| Environment | virtualenv (venv) | — | Isolated Python environment |
| OS | Windows 11 | — | Development platform |

#### Why These Tools?

- **pytesseract** — Official Python wrapper for Google's Tesseract, the world's most accurate open-source OCR engine. Uses a CNN + BiLSTM architecture internally.
- **OpenCV** — The industry standard computer vision library. Handles all image transformations (grayscale, blur, threshold, drawing).
- **Tesseract v5** — Introduced LSTM-based recognition (OEM 3), significantly more accurate than the legacy pattern-matching approach in older versions.

---

### ⚙️ Pre-Processing Pipeline {#-pre-processing-pipeline-p4}

Raw images contain shadows, chromatic noise, uneven lighting, and micro-imperfections that confuse OCR engines. The pipeline cleans them systematically:

#### Step 1 — Grayscale Conversion
```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
Collapses the 3D RGB array `(H, W, 3)` into a 1D intensity matrix `(H, W)`. Removes all color information — OCR does not need color, and color adds noise.

#### Step 2 — Denoising
```python
denoised = cv2.fastNlMeansDenoising(gray, h=10)
```
Applies Non-Local Means Denoising. Removes random pixel-level noise by averaging similar pixel neighborhoods across the image.

#### Step 3 — CLAHE Contrast Enhancement
```python
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
contrast = clahe.apply(denoised)
```
**Contrast Limited Adaptive Histogram Equalization** — enhances local contrast across different regions of the image independently. Critical for documents with uneven lighting or faded ink.

#### Step 4 — Gaussian Blur
```python
blurred = cv2.GaussianBlur(contrast, (3, 3), 0)
```
Smooths remaining micro-imperfections using a 3×3 Gaussian kernel. Eliminates artifact noise before the thresholding step.

#### Step 5 — Adaptive Thresholding (Otsu's Method)
```python
thresh = cv2.adaptiveThreshold(
    blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize=11, C=2
)
```
Forces every pixel to choose a side — **black (0) or white (255)**. Unlike global thresholding, adaptive thresholding calculates the cutoff value locally for different regions, handling uneven lighting perfectly.

```
The Math (Otsu's Method):
IF pixel_intensity >= threshold → pixel = 255 (White / Foreground)
IF pixel_intensity < threshold  → pixel = 0   (Black / Background)
```

**Before:** Grayscale image with shadows and noise
**After:** Pure binary image with crisp, high-contrast character contours — ideal for OCR

---

### 🎯 Confidence Filtering — The 80% Threshold

Every word detected by Tesseract comes attached to a **confidence score (0–100%)** — the engine's own assessment of how certain it is about that detection.

#### The Risk Without Filtering

Without a confidence filter, an AI treats every guess with equal certainty, producing hallucinations and false positives (the initial run returned `|`, `(`, `=`, `Bs` as "detected words").

#### The Implementation

```python
CONFIDENCE_THRESHOLD = 80  # Project 4 minimum requirement

for i in range(len(data['text'])):
    word = data['text'][i].strip()
    conf = int(data['conf'][i])

    if word and conf >= CONFIDENCE_THRESHOLD:
        # Accept this detection
        extracted_words.append(word)
        draw_bounding_box(i)
    else:
        # Drop this detection
        pass
```

#### The Trade-off

| Threshold | Effect |
|-----------|--------|
| Low (< 60%) | More words found, more false positives |
| Medium (60–79%) | Balanced but still includes noise |
| **High (≥ 80%)** | **Fewer words, but all genuine — Project 4 standard** |
| Very High (> 95%) | May miss valid words in imperfect images |

**80% is the absolute minimum standard for this project.**

---

### ✅ Milestone Validations

Project 4 requires passing four uncompromising technical validations (The Gatekeeper Rule):

| # | Validation | Requirement | Status |
|---|-----------|-------------|--------|
| 1 | **Library Integration** | Error-free implementation of pytesseract + cv2 | ✅ PASSED |
| 2 | **Pre-Processing Integrity** | Demonstrable grayscale conversion + adaptive thresholding | ✅ PASSED |
| 3 | **Accuracy Benchmarking** | Minimum 80% validated confidence score on output | ✅ PASSED |
| 4 | **Visual Confirmation** | Legible OCR output with accurate bounding boxes and labels | ✅ PASSED |

---

### 📁 Project Structure {#-project-structure-p4}

```
4project/
│
├── ocr_pipeline.py          # Main pipeline script
├── sample.png               # Input image (your test image goes here)
├── preprocessed.png         # Auto-generated: result after pre-processing
├── output_result.png        # Auto-generated: original image + bounding boxes
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

### 🚀 Installation Guide {#-installation-guide-p4}

#### Prerequisites

- Python 3.11.0
- Windows OS (instructions below are Windows-specific)
- Tesseract OCR Engine (separate install — see Step 2)

---

#### Step 1 — Clone the Repository

```bash
git clone https://github.com/akmalvizo/ocr-text-recognition-pipeline.git
cd ocr-text-recognition-pipeline
```

#### Step 2 — Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

#### Step 3 — Install Python Dependencies

```bash
pip install opencv-python
pip install pytesseract
pip install pillow
```

Or install all at once:
```bash
pip install -r requirements.txt
```

**requirements.txt contents:**
```
opencv-python
pytesseract
pillow
```

#### Step 4 — Install Tesseract OCR Engine

Tesseract is a separate system-level program that pytesseract wraps. It must be installed independently.

1. Download the Windows installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the `.exe` installer → keep clicking Next
3. Note the install path (default: `C:\Program Files\Tesseract-OCR\`)
4. **Add to PATH:** Win + S → "Environment Variables" → System Variables → Path → New → paste `C:\Program Files\Tesseract-OCR`
5. Restart your terminal

**Verify installation:**
```bash
tesseract --version
# Expected: tesseract 5.5.0.20241111
```

#### Step 5 — Verify Python Libraries

```bash
python -c "import cv2; print('OpenCV OK:', cv2.__version__)"
python -c "import pytesseract; print('pytesseract OK')"
```

---

### ▶️ How to Run

#### 1. Add Your Input Image

Place any image with printed text in the project folder and name it `sample.png`.

**Best image types:**
- Screenshot of a document or webpage
- Photo of a printed book page or invoice
- Any image with clear, typed (not handwritten) text

#### 2. Run the Pipeline

```bash
python ocr_pipeline.py
```

#### 3. Check Outputs

| File | Description |
|------|-------------|
| Console output | Word-by-word detection with confidence scores |
| `preprocessed.png` | Image after the 5-step cleaning pipeline |
| `output_result.png` | Original image with green bounding boxes + confidence labels |

---

### 📊 Sample Output {#-sample-output-p4}

```
Script started...
[OK] OpenCV loaded: 4.13.0
[OK] pytesseract loaded
[OK] Tesseract engine found: version 5.5.0.20241111
[OK] Image loaded successfully: (1080, 1920, 3)
Running pre-processing pipeline...
[OK] Step 1: Grayscale conversion done
[OK] Step 2: Denoising done
[OK] Step 3: Contrast enhancement done
[OK] Step 4: Gaussian blur applied
[OK] Step 5: Adaptive thresholding done
[OK] preprocessed.png saved

Running OCR (confidence threshold: 80%)...
[OK] OCR completed
====================================================
RESULTS — Words with 80%+ Confidence:
====================================================
  Word: 'Invoice'     | Confidence: 96%
  Word: 'Date'        | Confidence: 91%
  Word: 'Total'       | Confidence: 88%
  Word: '499.00'      | Confidence: 83%
====================================================
Full Extracted Text:
Invoice Date Total 499.00

[OK] output_result.png saved (bounding boxes drawn)

====================================================
PROJECT 4 — MILESTONE VALIDATION SUMMARY
====================================================
  [1] Library Integration     : PASSED (cv2 + pytesseract)
  [2] Pre-Processing Integrity: PASSED (grayscale + threshold)
  [3] Accuracy Benchmarking   : PASSED (80% threshold applied)
  [4] Visual Confirmation     : PASSED (output_result.png)
====================================================
[DONE] Pipeline complete!
```

---

### 📖 PSM Mode Guide

PSM (Page Segmentation Mode) tells Tesseract how your text is laid out. Choose based on your input image:

| PSM | Flag | Best For |
|-----|------|----------|
| 3 | `--psm 3` | Fully automatic — varied layouts (default) |
| 6 | `--psm 6` | Single uniform block of text — book pages, paragraphs |
| 7 | `--psm 7` | Single text line — number plates, headers |
| 11 | `--psm 11` | Sparse, scattered text — invoices, forms |

To change PSM mode, update this line in `ocr_pipeline.py`:

```python
custom_config = r'--oem 3 --psm 6'   # Change 6 to your required mode
```

**OEM (OCR Engine Mode):**
- `--oem 3` = Use both LSTM and Legacy engine (recommended, most accurate)

---

### 💡 Key Learnings {#-key-learnings-p4}

#### Technical Concepts Mastered

- **Machine Perception** — Understanding that images are 3D numerical arrays and every visual transformation is a mathematical operation on those arrays
- **Transfer Learning in Practice** — Using Tesseract's pre-trained convolutional + BiLSTM model instead of training from scratch
- **Image Pre-Processing** — Why raw visual data cannot go directly into an AI model and how each cleaning step (grayscale → denoise → CLAHE → blur → threshold) removes specific types of noise
- **Confidence Thresholding** — The engineering decision behind setting a minimum confidence gate and how it prevents hallucinations
- **Bounding Box Coordinates** — How OCR engines output normalized spatial coordinates `(X, Y, W, H)` and how to translate them into pixel-space overlays
- **PSM Tuning** — How layout configuration directly impacts OCR accuracy for different document types

#### Debugging Experience

| Problem | Root Cause | Fix Applied |
|---------|-----------|-------------|
| `ModuleNotFoundError: cv2` | Library not installed in venv | `pip install opencv-python` inside activated venv |
| `ModuleNotFoundError: pytesseract` | Library not installed | `pip install pytesseract` |
| `tesseract not recognized` | Tesseract not on system PATH | Added `C:\Program Files\Tesseract-OCR` to Windows PATH |
| OCR returning `\|` symbols | Image too large (3707×5024), raw noise detected as characters | Added auto-resize to 2000px + single-char filter |
| Low confidence on all words | Adaptive threshold blockSize too large | Tuned to `blockSize=11, C=2` for better binary separation |

---

### 🏢 About the Internship

This project was built as part of the **DecodeLabs AI Engineering Industrial Training Program — Batch 2026**.

| Detail | Info |
|--------|------|
| Program | AI Engineering Internship |
| Organization | DecodeLabs |
| Batch | 2026 |
| Project Number | 4 (Optional Mastery Phase) |
| Track | Image & Text Recognition (Basic) |
| Type | Virtual / Remote |

#### All 4 DecodeLabs Projects

| # | Project | Key Tech |
|---|---------|----------|
| 1 | **Vizo AI** — Rule-based Python chatbot | 17 intent categories, zero external dependencies |
| 2 | **Iris Flower Classifier** — KNN pipeline | Scikit-learn, feature scaling, confusion matrix, F1 score |
| 3 | **Tech Stack Recommender** — Content-based engine | TF-IDF, cosine similarity, 18 job role matching |
| 4 | **OCR Pipeline** — Text recognition system | pytesseract, OpenCV, adaptive thresholding, confidence filtering |

---

---

## 📈 Skills Progression Across Projects

| Skill Area | Project 1 | Project 2 | Project 3 | Project 4 |
|---|---|---|---|---|
| Python Fundamentals | ✅ Core | ✅ Applied | ✅ Applied | ✅ Applied |
| Data Structures | ✅ Dictionaries | ✅ DataFrames | ✅ Vectors | ✅ Arrays / Pixel Matrices |
| Machine Learning | ❌ Rule-based | ✅ KNN | ✅ TF-IDF | ✅ Transfer Learning (Tesseract) |
| Algorithm Design | ✅ O(1) lookup | ✅ Elbow Method | ✅ Cosine Similarity | ✅ Confidence Thresholding |
| Evaluation Metrics | ❌ | ✅ F1, Confusion Matrix | ✅ Similarity Score | ✅ OCR Confidence Score |
| Libraries Used | Standard Library only | scikit-learn, pandas | scikit-learn, pandas | OpenCV, pytesseract, Pillow |
| AI Type | Deterministic / White Box | Probabilistic / Supervised | Content-Based / Unsupervised | Machine Perception / Transfer Learning |

---

## 🔮 Future Roadmap

- Expand Vizo AI with conversation memory and a Flask web frontend
- Benchmark KNN against Decision Trees, SVM, and Logistic Regression
- Grow the Tech Stack Recommender to 50+ job roles with hybrid filtering
- Deploy all three projects as live web applications
- Implement cross-validation for more robust ML evaluation
- Extend the OCR Pipeline to handle handwritten text recognition
- Add multi-language OCR support beyond English

---

## 📄 License

All projects were created as part of the **DecodeLabs Industrial Training Program**.
© 2026 Muhammad Akmal · DecodeLabs Batch 2026

---

<p align="center">
  Built with 💚 during the DecodeLabs AI Industrial Training Program<br>
  <em>"An LLM without rules is a hallucination engine. This project builds the skeleton that holds the intelligence." — DecodeLabs</em>
</p>
