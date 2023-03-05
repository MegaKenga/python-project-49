import prompt
from brain_games.cli import greeting
from brain_games.utils import transform_bool, str_result, wrong_answer
from brain_games.utils import right_answer

TRIES = 3


def run_engine(current_game, description):
    name = greeting()
    count_of_tries = 0
    print(description)
    while count_of_tries < TRIES:
        question, result, type_result = current_game()
        result = transform_bool(type_result, result)
        result = str_result(result)
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != result:
            return wrong_answer(answer, result, name)
        right_answer()
        count_of_tries += 1

    print(f'Congratulations, {name}!')
