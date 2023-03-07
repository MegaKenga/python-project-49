from brain_games.utils import random_number
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def check_gcd():
    number1 = random_number()
    number2 = random_number()
    result = gcd(number1, number2)
    type_result = type(result)
    question = (f'Question: {number1} {number2}')
    return question, result, type_result
