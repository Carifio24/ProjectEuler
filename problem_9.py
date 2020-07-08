####################################################
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
####################################################

# We have c = 1000 - a - b
# So c^2 = (1000 - a - b)^2 = 1000^2 + a^2 + b^2 + 2ab - 2000a - 2000b

# Combining this with the Pythagorean relation gives
# a^2 + b^2 = 1000^2 + a^2 + b^2 + 2ab - 2000a - 2000b
# or
# 2ab - 2000(a+b) + 1000^2 = 0

# Solving for a gives
# a = 1000(b-500)/(b-1000)

# We want a to be an natural number, so b has to be below 500, so that a is positive
# We also want a < b, so
# b > 1000(b-500)/(b-1000)
# This has a solution 1000 - 500 * sqrt(2) < b < 1000, so b > 1000 - 500 *sqrt(2) = 292.9

# This gives us a scan range for b, 293 <= a < 500, for which the expression for a is an integer

from math import floor, sqrt

b_min = 293
b_max = 499
for b in range(b_min, b_max+1):
    a = 1000 * (b - 500) / (b - 1000)
    if (a == floor(a)):
        a = int(a)
        break

c = int(sqrt(pow(a,2) + pow(b,2)))
print(a*b*c)