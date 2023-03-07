from brain_games.utils import random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_check():
    number = random_number()
    result = number % 2 == 0
    type_result = type(result)
    question = (f'Question: {number}')
    return question, result, type_result
