
###################################################
# A lot of these problems involve similar computations
# So I've saved some useful ones here for convenience
####################################################

import operator
from functools import reduce
from math import floor, sqrt, gcd

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
            q = x // i
            if q != i:
                facs.append(q)
    return facs

# Get the digits of a number
# Returned in the order [ ones, tens, hundreds, ... ]
def digits(x):
    digits = []
    while x > 0:
        r = x % 10
        digits.append(r)
        x = (x - r) // 10
    return digits

# Get the lcm of a list of numbers
def lcm_seq(seq):
    if len(seq) == 0:
        return 1
    if len(seq) == 1:
        return seq[0]
    elif len(seq) == 2:
        return lcm(*seq)
    else:
        return lcm_seq([ lcm(seq[0], seq[1]) ] + seq[2:])

# Get the lcm of two numbers
def lcm(a, b):
    return abs(a*b) // gcd(a, b)