from question_model import Pergunta
from data import question_data
from quiz_brain import QuizBrain 

banco_de_perguntas = []
for pergunta in question_data:
        pergunta = Pergunta(pergunta['text'],pergunta['answer'])
        banco_de_perguntas.append(pergunta)

quiz = QuizBrain(banco_de_perguntas)
while quiz.remain():
        quiz.next_question()