import pandas as pd

data = {
    "cleaned_text": [
        "python machine learning pandas",
        "deep learning tensorflow pytorch",
        "recruitment onboarding hr"
    ],
    "category": [
        "Data Scientist",
        "ML Engineer",
        "HR"
    ]
}

df = pd.DataFrame(data)

df.to_csv("G:/HireSense-AI/data/processed/cleaned_resumes.csv", index=False)

print("✅ CSV file created!")
