from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

qa_df = pd.read_csv('model/qa_data.csv')
questions = qa_df['q2'].tolist()
answers = qa_df['q1'].tolist()

question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_embedding(text):
    return model.encode(text, convert_to_tensor=True)

def get_all():
    return questions, question_embeddings, answers
