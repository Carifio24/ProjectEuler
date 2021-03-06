####################################################
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
####################################################

from euler import is_prime, factors

# Get the factors of x
def get_factors(x):
    global cached_factors
    if x in cached_factors:
        return cached_factors[x]

    facs = factors(x)
    cached_factors[x] = facs
    return facs

# Do the calculation
# To avoid redundant calculations, we cache answers
cached_factors = {}
facs = sorted(factors(600851475143), reverse=True)
for x in facs:
    if is_prime(x):
        print(x)
        break

