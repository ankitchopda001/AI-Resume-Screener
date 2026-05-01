from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def train_vectorizer(corpus):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(corpus)
    joblib.dump(vectorizer, "G:/HireSense-AI/models/tfidf.pkl")
    return X, vectorizer

def load_vectorizer():
    return joblib.load("G:/HireSense-AI/models/tfidf.pkl")


# Removes symbols
# Removes stopwords
# Makes text ML-ready