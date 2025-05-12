from model.embedder import get_embedding, get_all
from sentence_transformers.util import cos_sim

def find_best_answer(user_question):
    questions, embeddings, answers = get_all()
    user_embedding = get_embedding(user_question)
    similarities = cos_sim(user_embedding, embeddings)[0]
    best_idx = similarities.argmax().item()
    return answers[best_idx]
