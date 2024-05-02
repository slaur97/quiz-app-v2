import html
class run_questions:
    def __init__(self,questions):
        self.questions=questions
        self.number_questions=-1
        self.score=0
    def next_question(self):
        self.number_questions+=1
        return html.unescape(str(self.number_questions+1)+"."+self.questions[self.number_questions].questions)
    def next_answers(self):
        return html.unescape(self.questions[self.number_questions].incorrect_answer)
        
    def correct_answers(self):
        return html.unescape(self.questions[self.number_questions].correct_answer)
        
    



