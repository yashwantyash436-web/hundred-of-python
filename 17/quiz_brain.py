class quizbuzz:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def is_question_left(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(ans, current_question.answer)

    def check_answer(self, ans, correct_answer):
        if ans.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")

        print(f"Score: {self.score}/{self.question_number}")