
###################################################
# A lot of these problems involve similar computations
# So I've saved some useful ones here for convenience
####################################################

from math import floor, sqrt

# Check whether x is prime
def is_prime(x):
    for i in range(2, floor(sqrt(x))+1):
        if x % i == 0:
            return False
    return True