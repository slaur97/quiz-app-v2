import random
from api import data
from questions import Questions
from functionality import run_questions
from graphic import win

objects=[]
for element in data:
    questions=element['question']
    incorrect_answer=element['incorrect_answers']
    incorrect_answer.append(element["correct_answer"])
    random.shuffle(incorrect_answer)
    correct_answer=element["correct_answer"]
    object_increment=Questions(questions,incorrect_answer,correct_answer)
    objects.append(object_increment)

object=run_questions(objects)
graphic=win(object)


