from brain_games.calculations import random_even

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def even_check():
    number, result = random_even()
    question = (f'Question: {number}')
    return question, result
