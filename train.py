import pandas as pd
from src.preprocessing.clean_text import clean_text
from src.feature_engineering.tfidf_vectorizer import train_vectorizer
from src.models.classifier import train_classifier

# Load dataset
df = pd.read_csv("G:/HireSense-AI/data/processed/cleaned_resumes.csv")

# Cleam Text
df["cleaned_text"] = df["cleaned_text"].apply(clean_text)

# Train vectorizer 
X, vectorizer = train_vectorizer(df["cleaned_text"])

# Train classifier 
train_classifier(X, df["category"])

print("Model training and saved!")

# Loads CSV (training data)
# Cleans text
# Converts to vectors (TF-IDF)
# Trains classification model