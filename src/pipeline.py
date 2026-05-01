from src.preprocessing.clean_text import clean_text
from src.feature_engineering.tfidf_vectorizer import load_vectorizer
from src.models.classifier import load_classifier
from src.models.similarity import compute_similarity

def process(resume_text, job_text):
    vectorizer = load_vectorizer()
    classifier = load_classifier()

    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    resume_vec = vectorizer.transform([resume_clean])
    job_vec = vectorizer.transform([job_clean])

    role = classifier.predict(resume_vec)[0]
    score = compute_similarity(resume_vec, job_vec)

    return role, score

# This is the main brain

# Takes input
# Runs full ML pipeline
# Returns result

# This connects everything