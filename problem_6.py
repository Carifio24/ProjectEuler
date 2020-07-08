# ####################################################
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
####################################################

from math import gcd

# Get the least common multiple of two numbers
# We'll just use the built-in gcd, it's not worth writing out Euclid's algorithm or something
def lcm(x,y):
    return x * y // gcd(x,y)


# We are given that 2520 is the result for 1-10
# So let's start there
value = 2520
for i in range(11,21):
    value = lcm(value, i)

print(value)