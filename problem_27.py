####################################################
# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000, where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
####################################################

# Basic observations:
# We only need to consider when b is prime, otherwise the n = 0 case fails for any a
# This means that b >= 2
# The roots of n^2 + an + b are -a/2 +/- sqrt(a^2-4b) / 2
# If one of these roots is positive, obviously it serves as an upper bound on the maximum number of primes
# We can use this once we get a maximum value

# Only happens when a, b have opposite signs - i.e. a < 0
# If a < 0, then the roots are |a|/2 +/- sqrt(a^2-4b)
# The bound is the minimum positive number of these values

# Beyond that, it's just plug-and-check

from math import floor, sqrt
from euler import is_prime

n_max = 0
a_max = 0
b_max = 0
for b in range(2, 1000):

    # As discussed above, we need b to be prime
    if not is_prime(b):
        continue

    # Loop over possible a values
    for a in range(1, 1000):

        # Try the positive number
        n = 1
        value = 1 + a + b
        while is_prime(value):
            n += 1
            value = n * n + a * n + b
        if n > n_max:
            n_max = n
            a_max = a
            b_max = b
        
        # Same for the negative, enforcing the check discussed above
        disc = a * a - 4 * b
        real_roots = disc >= 0
        if real_roots:
            r1 = a - disc
            r2 = a + disc
            min_pos_root = r1 if r1 > 0 else r2
        if real_roots and min_pos_root < n_max:
            continue

        n = 1
        value = 1 - a + b
        while value > 0 and is_prime(value):
            n += 1
            value = n * n - a * n + b
        if n > n_max:
            n_max = n
            a_max = -a
            b_max = b


print(n_max)
print(a_max * b_max)