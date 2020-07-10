
###################################################
# A lot of these problems involve similar computations
# So I've saved some useful ones here for convenience
####################################################

import operator
from functools import reduce
from math import floor, sqrt

# Check whether x is prime
def is_prime(x):
    for i in range(2, floor(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# Find the product of the entries of an iterable sequence
def product(iterable):
    return reduce(operator.mul, iterable, 1)

# Get the factors of x
def factors(x):
    facs = []
    for i in range(1, floor(sqrt(x))+1):
        if x % i == 0:
            facs.append(i)
            facs.append(x / i)
    return facs