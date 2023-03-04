from random import randint, choice

RANDOM_NUMBER_MIN = 0
RANDOM_NUMBER_MAX = 100
OPERATORS_LIST = ['+', '-', '*']
YES = 'yes'
NO = 'no'


def str_result(result):
    result = str(result)
    return result


def right_answer():
    print('Correct!')


def wrong_answer(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'. Let's try again, {name}!")


def random_number():
    return randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)


def random_operator():
    return choice(OPERATORS_LIST)


def transform_bool(type_result, result):
    if type_result == bool:
        if result is True:
            result = YES
        elif result is False:
            result = NO
        return result
    elif type_result == int:
        return result
