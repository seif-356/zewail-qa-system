# Zewail City QA System (Flask)

## Setup
```bash
pip install -r requirements.txt
```

## Run the App
```bash
python app.py
```

## Description
This web app takes a user question and matches it to known Zewail City Q&A using a Siamese model with transformers.

Make sure `model/qa_data.csv` contains your question-answer pairs with columns `q2` (known questions) and `q1` (answers).
