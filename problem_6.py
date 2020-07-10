# ####################################################
# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385

# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
####################################################

# The sum of the first n natural numbers is the triangular number n * (n + 1) /2, so for 100 it's 50 * 101 = 5050

# I don't recall offhand a formula for the sum of the squares of the first n natural numbers, but since the forward differences are squares, the third forward difference are constant
# In other words, there should be a cubic that describes the sums
# So let's find it

# Define our cubic as an^3 + bn^2 + cn + d
# The sum of the first 0 cubes is 0, so d = 0

# n = 1:
# 1^2 = 1
# so a + b + c = 1

# n = 2:
# 1^2 + 2^2 = 1 + 4 = 5
# so 8*a + 4*b + 2*c = 5

# n = 3:
# 1^2 + 2^2+ 3^2 = 5 + 3^2 = 14
# so 27*a + 9*b + 3*c = 14

# Solving this is just some basic linear algebra, giving us
# a = 1/3, b=1/2, c = 1/6

# So the sum of the first n squares is 2n^3 - (5/2)n^2 + (3/2)n

# From here, the calculation is trivial

def sum_of_first_n_naturals(n):
    return (n * (n + 1)) // 2

def sum_of_first_n_squares(n):
    return (2 * pow(n,3) + 3 * pow(n,2) + n) // 6



n = 100
result = pow(sum_of_first_n_naturals(n),2) - sum_of_first_n_squares(n)
print(result)