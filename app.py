from flask import Flask, request, render_template
from model.qa_model import find_best_answer
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        user_question = request.form['question']
        answer = find_best_answer(user_question)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
