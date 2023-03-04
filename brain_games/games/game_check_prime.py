from brain_games.calculations import random_prime


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def check_prime():
    number, result, type_result = random_prime()
    question = (f'Question: {number}')
    return question, result, type_result
