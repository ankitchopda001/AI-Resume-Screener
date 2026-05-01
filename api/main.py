from fastapi import FastAPI
from src.pipeline import process

app = FastAPI()

@app.get("/")
def home():
    return {"message": "HireSense AI is running!"}

@app.post("/predict/")
def predict(resume: str, job:str):
    role, score = process(resume, job)
    return {"Role": role, "Score": score}

# Converts project into API
# Can be used in real apps