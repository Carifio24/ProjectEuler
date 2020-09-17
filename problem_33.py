####################################################
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
####################################################

# It's clear that the erroneously canceled digit must be in opposite positions on the top and the bottom
# Suppose the digit, call it x, were in the same place in the top and bottom
# First, say the tens place:
# We would then have (10 * x + m) / (10 * x + n) == m / n
# 10 * n * x + m * n == 10 * m * x + m * n    --->    m == n (i.e., the fraction is 1) or x == 0 (trivial case)
# 
# Now the ones place:
# (10 * m + x) / (10 * n + x) == m / n
# 10 * m * n + x * n == 10 * m * n + x * m    -->    m == n (i.e., the fraction is 1) or x == 0 (trivial case)

# So the repeated digit is opposite places
# Also note that the denominator must be more than the numerator

from euler import digits, product
from math import gcd

# Find the numerators and denominators of the fractions that satisfy this
fracs = set()
for num in range(10, 100):
    num_digs = digits(num)
    for den in range(num + 1, 100):
        den_digs = digits(den)

        # Skip the 'trivial' cases
        if num_digs[0] == 0 and den_digs[0] == 0:
            continue

        # If we have matching digits
        if num_digs[0] == den_digs[1]:
            if (num * den_digs[0] == den * num_digs[1]):
                fracs.add((num_digs[1], den_digs[0]))
        if num_digs[1] == den_digs[0]:
            if (num * den_digs[1] == den * num_digs[0]):
                fracs.add((num_digs[0], den_digs[1]))


# Once we've got the fractions, we need to find the product and get its reduced denominator
# We first find the lcm of the fraction denominators
prod_num = product(x[0] for x in fracs)
prod_den = product(x[1] for x in fracs)
g = gcd(prod_num, prod_den)
print(prod_den // g)