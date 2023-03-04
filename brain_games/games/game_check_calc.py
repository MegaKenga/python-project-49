from brain_games.calculations import random_calc


DESCRIPTION = 'What is the result of the expression?'


def check_calc():
    number1, number2, calc, result, type_result = random_calc()
    question = (f'Question: {number1} {calc} {number2}')
    return question, result, type_result
