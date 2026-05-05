class QuizBrain:
    """Handles quiz logic, question flow, and score tracking."""

    def __init__(self, question_list):
        """Initialize quiz state with a list of questions."""
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        """Return True if there are remaining questions to ask."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Return the current question and increment the question number."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return self.current_question

    def check_answer(self, user_answer):
        """Check the user's answer and update the score if correct."""
        correct_answer = self.current_question.answer.lower()
        is_correct = user_answer == correct_answer
        if is_correct:
            self.score += 1
        return is_correct
