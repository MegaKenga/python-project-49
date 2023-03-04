from brain_games.calculations import random_progression

DESCRIPTION = 'What number is missing in the progression?'


def check_progression():
    new_line, result, type_result = random_progression()
    question = (f'Question: {new_line}')
    return question, result, type_result
