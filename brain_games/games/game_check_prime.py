from brain_games.utils import random_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime():
    prime_count = 0
    number = random_number()
    for i in range(1, number + 1):
        if number % i == 0:
            prime_count += 1
    result = prime_count == 2
    type_result = type(result)
    question = (f'Question: {number}')
    return question, result, type_result
