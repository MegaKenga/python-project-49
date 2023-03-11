import prompt
from brain_games.cli import greeting
from brain_games.utils import get_result, wrong_answer, right_answer

TRIES = 3


def run_engine(current_game, description):
    name = greeting()
    count_of_tries = 0
    print(description)
    while count_of_tries < TRIES:
        question, result, type_result = current_game()
        result = get_result(type_result, result)
        print(question)
        answer = prompt.string('Your answer: ')
        if answer.lower() != result:
            return wrong_answer(answer, result, name)
        right_answer()
        count_of_tries += 1

    print(f'Congratulations, {name}!')
