from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

DEBUG = False


def get_user_answer(question, q_number):
    """Prompt the user until a valid True/False answer is given."""
    while True:
        user_input = input(f"\nQ.{q_number}: {question.text} (True/False)?: ").strip().lower()

        if user_input in ("true", "false"):
            return user_input

        print("That's not a valid input. Please try again.")


def handle_feedback(quiz, user_response, question):
    """Display whether the answer was correct and show current score."""
    if quiz.check_answer(user_response):
        print("You got it right!")
    else:
        print("That's wrong.")

    print(f"The correct answer was: {question.answer}.\n"
          f"Your current score is {quiz.score}/{quiz.question_number}.")


def quiz_game():
    """Run the quiz game loop."""
    question_bank = [Question(item["text"], item["answer"]) for item in question_data]
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        current_question = quiz.next_question()

        if DEBUG:
            print(f"\n[DEBUG] Q{quiz.question_number} answer: {current_question.answer}")

        user_answer = get_user_answer(current_question, quiz.question_number)
        handle_feedback(quiz, user_answer, current_question)

    print(f"\nYou've completed the quiz.\n"
          f"Your final score was {quiz.score}/{len(question_bank)}.")


quiz_game()
