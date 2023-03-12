import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
j=0
while j<len(question_data[0]["results"]:
  for i in question_data:
    question_text = i["results"][j]["question"]
    question_answer = i["results"][j]["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
     j+=1

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
