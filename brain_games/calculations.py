from random import randint
from math import gcd
from brain_games.utils import random_number, random_operator


def random_even():
    number = random_number()
    result = number % 2 == 0
    return number, result

def random_prime():
    prime_count = 0
    number = random_number()
    for i in range(1, number + 1):
        if number % i == 0:
            prime_count += 1
    result = prime_count == 2
    return number, result

def random_progression():
    init_number = randint(0, 3)
    step = randint(2, 4)
    length = step * 10
    line = []
    for i in range(init_number, length, step):
        line.append(i)
    random_index = randint(1, (len(line) - 1))
    result = line[random_index]
    line[random_index] = '..'
    new_line = " ".join(map(str, line))
    return new_line, result

def random_calc():
    number1 = random_number()
    number2 = random_number()
    calc = random_operator()
    if calc == '+':
        result = number1 + number2
    elif calc == '-':
        result = number1 - number2
    elif calc == '*':
        result = number1 * number2
    return number1, number2, calc, result

def random_gcd():
    number1 = random_number()
    number2 = random_number()
    result = gcd(number1, number2)
    return number1, number2, result
