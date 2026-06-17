import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── STEP 1: INGESTION ──────────────────────────────────────
# Load the dataset
df = pd.read_csv("raw_skills.csv")

print("=" * 50)
print("   Welcome to the Tech Stack Recommender")
print("=" * 50)
print("\nEnter at least 3 skills (comma-separated).")
print("Example: Python, SQL, Machine Learning\n")

user_input = input("Your skills: ")

# Parse user input into a clean string
user_skills = [s.strip() for s in user_input.split(",")]

if len(user_skills) < 3:
    print("Please enter at least 3 skills!")
    exit()

# Convert user skills to a single string (same format as dataset)
user_profile = ", ".join(user_skills)

# ── STEP 2: SCORING ────────────────────────────────────────
# Combine user profile + all job role skills into one list
all_documents = df["skills"].tolist() + [user_profile]

# Apply TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_documents)

# User vector is the last one
user_vector = tfidf_matrix[-1]

# Job role vectors are all except the last
job_vectors = tfidf_matrix[:-1]

# Calculate cosine similarity between user and each job role
scores = cosine_similarity(user_vector, job_vectors).flatten()

# ── STEP 3: SORTING ────────────────────────────────────────
# Add scores to dataframe and sort descending
df["similarity_score"] = scores
df_sorted = df.sort_values("similarity_score", ascending=False)

# ── STEP 4: FILTERING (Top 3) ──────────────────────────────
top_n = 3
top_results = df_sorted.head(top_n)

# ── OUTPUT ─────────────────────────────────────────────────
print("\n" + "=" * 50)
print(f"   Top {top_n} Recommended Career Paths For You")
print("=" * 50)

for rank, (_, row) in enumerate(top_results.iterrows(), start=1):
    match_percent = round(row["similarity_score"] * 100, 2)
    print(f"\n#{rank} {row['job_role']}")
    print(f"   Match Score : {match_percent}%")
    print(f"   Key Skills  : {row['skills']}")

print("\n" + "=" * 50)
print("Recommendation complete. Good luck!")
print("=" * 50)