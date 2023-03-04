from random import randint, choice

RANDOM_NUMBER_MIN = 0
RANDOM_NUMBER_MAX = 100
OPERATORS_LIST = ['+', '-', '*']
YES = 'yes'
NO = 'no'

def check_answer(answer):
    return type(answer) is int

def str_result(answer, result):
    result = str(result)
    answer = str(answer)
    return result, answer

def right_answer():
    print('Correct!')

def wrong_answer(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'. Let's try again, {name}!")

    
def random_number():
    return randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)

def random_operator():
    return choice(OPERATORS_LIST)

def transform_bool(check_answer, result):
    if  check_answer == False:
        if result == True:    
            return YES
        else:
            return NO
    else:
        pass
