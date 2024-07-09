class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def new_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}?(True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            print("you've complete all quiz.")
            print(f"your final score is: {self.user_score} / {len(self.question_list)}")
            return False
            
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("right")
            self.user_score += 1
        else:
            print("wrong")
            print(f"the correct answer is {correct_answer}.")

        print(f"your current score is: {self.user_score} / {self.question_number}")
        print("\n")

