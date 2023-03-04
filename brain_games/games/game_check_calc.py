from brain_games.calculations import random_calc


DESCRIPTION = 'What is the result of the expression?'

def check_calc():
    number1, number2, calc, result = random_calc()
    question = str(number1) + ' ' + str(calc) + ' ' + str(number2)
    return question, result
