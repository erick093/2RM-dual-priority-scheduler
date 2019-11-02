from functools import reduce
from math import gcd


def get_hyperperiod(tasks):
    hyperperiod = []
    for task in tasks:
        hyperperiod.append(task.period)
    hyperperiod = lcm(hyperperiod)
    return hyperperiod


def _lcm(a, b):
    return int(a * b / gcd(a, b))


def lcm(numbers):
    return reduce(_lcm, numbers)