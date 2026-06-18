# 🌸 Iris Flower Classification Using K-Nearest Neighbors (KNN)

> **DecodeLabs Industrial Training Kit — Batch 2026 | Project 2**  
> Data Classification Using Artificial Intelligence

---

## 📌 Project Overview

This project demonstrates a complete **Supervised Machine Learning pipeline** built from scratch using Python and Scikit-learn. The goal is to classify Iris flowers into one of three species — *Setosa*, *Versicolor*, or *Virginica* — based on their physical measurements, using the **K-Nearest Neighbors (KNN)** classification algorithm.

This project was completed as **Project 2** of the DecodeLabs AI Industrial Training Program (Batch 2026), focusing on core concepts of data handling, model training, and performance evaluation.

Run this iris_classification_model.ipynb file in Google Colab.

---

## 🎯 Objectives

- Load and explore a real-world benchmark dataset
- Preprocess data using Feature Scaling (StandardScaler)
- Split data into Training and Testing sets
- Train a KNN classification model
- Find the optimal value of K using the Elbow Method
- Evaluate the model using Confusion Matrix and F1 Score
- Make predictions on completely new, unseen data

---

## 🗂️ Project Structure

```
iris-knn-classification/
│
├── iris_classification.ipynb   # Main Colab Notebook (all steps)
├── README.md                   # Project documentation (this file)
└── requirements.txt            # Python dependencies
```

---

## 🧠 Concepts Covered

| Concept | Description |
|---|---|
| **Supervised Learning** | Training a model on labeled examples to predict unseen data |
| **Iris Dataset** | 150 samples, 3 classes, 4 features — the ML benchmark dataset |
| **Feature Scaling** | Normalizing features so no single variable dominates distance calculations |
| **Train-Test Split** | 80% training / 20% testing with shuffle to remove order bias |
| **KNN Algorithm** | Classifies by majority vote among K nearest data points |
| **Elbow Method** | Technique to find the optimal K value with lowest error rate |
| **Confusion Matrix** | Visual breakdown of correct and incorrect predictions per class |
| **F1 Score** | Harmonic mean of Precision and Recall — more reliable than raw accuracy |

---

## 📊 Dataset Information

The **Iris Dataset** is a classic benchmark dataset built into Scikit-learn.

| Property | Value |
|---|---|
| Total Samples | 150 (Balanced) |
| Classes | 3 (Setosa, Versicolor, Virginica) |
| Features | 4 (Sepal Length, Sepal Width, Petal Length, Petal Width) |
| Missing Values | None |
| Source | `sklearn.datasets.load_iris()` |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `scikit-learn` — Machine learning algorithms and utilities
  - `pandas` — Data manipulation and exploration
  - `numpy` — Numerical computations
  - `matplotlib` — Data visualization
  - `seaborn` — Statistical plotting (Confusion Matrix heatmap)
- **Environment:** Jupyter Notebook

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iris-knn-classification.git
cd iris-knn-classification
```

### 2. Install Dependencies

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

### 3. Launch Colab Notebook

```bash
Colab notebook iris_classification.ipynb
```

---

## 🔄 Pipeline Walkthrough

### Step 1 — Load & Explore the Dataset
```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
print(df.head())
print(df.describe())
```

### Step 2 — Feature Scaling
```python
from sklearn.preprocessing import StandardScaler

X = iris.data
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Step 3 — Train-Test Split
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, shuffle=True
)
```

### Step 4 — Train the KNN Model
```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Step 5 — Find Optimal K (Elbow Method)
```python
import numpy as np

error_rates = []
for k in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(preds != y_test))

best_k = error_rates.index(min(error_rates)) + 1
print("Optimal K:", best_k)
```

### Step 6 — Evaluate the Model
```python
from sklearn.metrics import confusion_matrix, f1_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title('Confusion Matrix')
plt.show()

f1 = f1_score(y_test, predictions, average='weighted')
print(f"F1 Score: {f1:.4f}")
print(classification_report(y_test, predictions, target_names=iris.target_names))
```

### Step 7 — Predict on New Data
```python
new_flower = [[5.1, 3.5, 1.4, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)
print("Predicted species:", iris.target_names[prediction[0]])
```

---

## 📈 Results

| Metric | Value |
|---|---|
| **Optimal K** | Found via Elbow Method |
| **F1 Score (Weighted)** | ~0.97+ |
| **Test Accuracy** | ~95–100% |

> The model achieves high performance on the Iris dataset because KNN with proper feature scaling is highly effective for well-separated, balanced classes.

---

## 🧩 Key Learnings

- Raw accuracy can be misleading on imbalanced datasets — F1 Score is more trustworthy
- Feature Scaling is critical for distance-based algorithms like KNN
- The Elbow Method helps avoid both overfitting (K=1) and underfitting (K=100)
- Shuffling before splitting removes order bias from the dataset
- A Confusion Matrix reveals exactly which classes are being confused by the model

---

## 🚀 Future Improvements

- [ ] Compare KNN against other classifiers (Decision Tree, SVM, Logistic Regression)
- [ ] Implement Cross-Validation (k-fold) for more robust evaluation
- [ ] Add data visualization (pair plots, feature distributions)
- [ ] Test the model on a custom CSV dataset beyond Iris
- [ ] Build a simple CLI interface for live predictions

---

## 🏢 About This Project

This project was built as part of the **DecodeLabs Industrial Training Program — Batch 2026**, under the Artificial Intelligence track. It represents the completion of **Project 2: Data Classification Using AI**, which serves as the foundational milestone for supervised learning in the program.

**Organization:** DecodeLabs  
**Track:** Artificial Intelligence  
**Project:** 2 of the Industrial Training Kit  
**Focus:** Supervised Learning, Data Classification, Model Validation

---

## 👤 Author

**Muhammad Akmal**  
AI Engineering Intern · DecodeLabs · Batch 2026

---

## 📄 License

This project was created as part of the DecodeLabs Industrial Training Program.  
© 2026 Muhammad Akmal · DecodeLabs Batch 2026

---

<p align="center">
  Built with 💚 during the DecodeLabs AI Industrial Training Program
</p>
