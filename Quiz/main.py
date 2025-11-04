
from data_bank import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []  # Stores questions

# Populate the question bank
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

