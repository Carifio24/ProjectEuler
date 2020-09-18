####################################################
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
####################################################

# A priori, any number from 1 to 987654321 with no repeating digits could be our product
# But in reality, the numbers on the larger end of this set aren't realizable, since there won't be enough digits in the multiplicand/multiplier to make them
# What's the largest value we could actually expect to get?
# The number of digits of a number x is given by floor(log10(x)) + 1 (note that ceil won't work - 10 has 2 digits, but log10(10) is exactly 1)

# So the number of digits of x * y is floor(log10(x*y)) + 1 = floor(log10(x) + log10(y)) + 1
# As a + b - 1 <= floor(a + b) <= a + b, the number of digits in x * y satisfies
# log10(x) + log10(y) <= ND(x * y) <= log10(x) + log10(y) + 1
# So the number of digits in x * y is at most equal to the sum of the number of digits of x and y
# and at least the sum of their digits minus 1
# in other words, it's one of these two numbers

# What does this mean for our product?
# Let the multiplicand be x, the multiplier be y, and the product be z
# Then ND(x) + ND(y) - 1 <= ND(z) <= ND(x) + ND(y)

# Our pandigital condition gives us another restraint - we only have 9 digits total
# so ND(x) + ND(y) + ND(z) == 9  --> ND(z) = 9 - ND(x) - ND(y)
# substituting this into the above gives

# ND(x) + ND(y) - 1 <= 9 - ND(x) - ND(y) <= ND(x) + ND(y)
# or
# ND(x) + ND(y) - 1/2 <= 9/2 <= ND(x) + ND(y)
# so ND(x) + ND(y) >= 4.5   and     ND(x) + ND(y) <= 5.5
# In other words, ND(x) + ND(y) = 5
# So we can reduce our scan space quite a bit

from itertools import permutations
from euler import from_digits

digits = [ x for x in range(1, 10) ]
products = set()
for perm in permutations(digits):
    p = list(perm)
    for ndx in range(1, 5):
        x = from_digits(p[:ndx])
        y = from_digits(p[ndx:5])
        z = from_digits(p[5:])
        if x * y == z:
            products.add(z)

print(sum(products))