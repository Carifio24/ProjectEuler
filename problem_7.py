
####################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
####################################################

from math import floor, sqrt

# Check whether x is prime
def is_prime(x):
    for i in range(2, floor(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


# Increase val, keeping track of each time we find a prime
# Terminate when we get to the 10,001st prime
val = 1
n_primes = 0
to_find = 10001
while n_primes < to_find:
    val += 1
    if is_prime(val):
        n_primes += 1


print(val)