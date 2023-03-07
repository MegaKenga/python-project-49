from random import randint

INIT_NUMBER = randint(0, 3)
STEP = randint(2, 4)
LENGTH = STEP * 10
DESCRIPTION = 'What number is missing in the progression?'


def check_progression():
    init_number = INIT_NUMBER
    step = STEP
    length = LENGTH
    line = []
    for i in range(init_number, length, step):
        line.append(i)
    random_index = randint(1, (len(line) - 1))
    result = line[random_index]
    line[random_index] = '..'
    new_line = " ".join(map(str, line))
    type_result = type(result)
    question = (f'Question: {new_line}')
    return question, result, type_result
