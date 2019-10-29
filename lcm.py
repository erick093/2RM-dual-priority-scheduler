from functools import reduce
from math import gcd


def _lcm(a, b):
    return int(a * b / gcd(a, b))


def lcm(numbers):
    return reduce(_lcm, numbers)