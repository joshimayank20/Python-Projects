class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number+1}: {question.text} (True/False): ")
        
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong.")
        
        self.question_number += 1

question_data = [
    Question("The sky is blue.", "True"),
    Question("2+2=5", "False"),
]

quiz = QuizBrain(question_data)

while quiz.question_number < len(question_data):
    quiz.next_question()

print("Final Score:", quiz.score)
