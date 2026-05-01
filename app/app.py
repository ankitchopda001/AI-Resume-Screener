import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.pipeline import process
from src.data_ingetion.parser import parse_pdf, parse_docx

st.title("HireSense AI")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    if uploaded_file.name.endswith(".pdf"):
        resume_text = parse_pdf(uploaded_file)
    else:
        resume_text = parse_docx(uploaded_file)

    role, score = process(resume_text, job_desc)

    st.subheader("Results")
    st.write(f"Predicted Role: {role}")
    st.write(f"Match Score: {round(score * 100, 2)}%")


# User uploads resume
# Shows prediction + score
