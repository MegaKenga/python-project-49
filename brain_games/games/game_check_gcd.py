from brain_games.calculations import random_gcd
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def check_gcd():
    number1, number2, result, type_result = random_gcd()
    question = (f'Question: {number1} {number2}')
    return question, result, type_result
