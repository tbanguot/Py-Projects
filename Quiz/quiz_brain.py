
class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.correct_answer = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        # Move to the next question
        self.question_number += 1
        # Prompt user to answer the question
        your_answer = input(f"Q.{self.question_number} {curr_question.text} True/False?: ")

        # Check the answer
        if your_answer.lower() == curr_question.answer.lower():
            self.correct_answer += 1
            print("You got it right!")
            print(f"The correct answer is {your_answer}")
            print(f"Your score is: {self.correct_answer}/{self.question_number}")
        else:
            print("Wrong Answer!")
            print(f"The correct answer is: {curr_question.answer}")
            print(f"Your score is: {self.correct_answer}/{self.question_number}")

        print()  # Print a blank line

    def still_has_question(self):
        return self.question_number < len(self.question_list)




