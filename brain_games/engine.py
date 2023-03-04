import prompt
from brain_games.cli import greeting
from brain_games.utils import check_answer, right_answer, wrong_answer, str_result, transform_bool

TRIES = 3


def run_engine(current_game, description):
    name = greeting()
    count_of_tries = 0
    print(description)
    while count_of_tries < TRIES:
        question, result = current_game()
        print(question)
        answer = prompt.string('Your answer: ')
        check_answer(answer)
        transform_bool(check_answer, result)
        str_result(answer, result)
        if answer != result:
            return wrong_answer(answer, result, name)
        right_answer()
        count_of_tries += 1
    
    print(f'Congratulations, {name}!')
