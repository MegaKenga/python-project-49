from brain_games.utils import random_number, random_operator

DESCRIPTION = 'What is the result of the expression?'


def check_calc():
    number1 = random_number()
    number2 = random_number()
    calc = random_operator()
    if calc == '+':
        result = number1 + number2
    elif calc == '-':
        result = number1 - number2
    elif calc == '*':
        result = number1 * number2
    type_result = type(result)
    question = (f'Question: {number1} {calc} {number2}')
    return question, result, type_result
