####################################################
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
####################################################

# First off, note that each time we add an extra 'layer' to the square, we're increasing its size by 2
# Because of this, the difference between numbers on the corners of each square layer increases by 2 each time
# i.e. for the 3-9 layer it's 2 between each corner, which is also the difference from 1:  1 -> 3 -> 5 -> 7 -> 9
# for the 10-13 layer it's 4, which is also the difference from the previous last corner: 9 -> 13 -> 17 -> 21 -> 25
# for the next layer it would be 6, and so on
# In terms of the square size, it's n - 1

# So for the layer with side length n, the sum is
# (c + (n+1)) + (c + 2*(n+1)) + (c + 3*(n+1)) + (c + 4*(n+1)) = 4 * c + 10 * (n-1)
# where c is the previous final corner

# As for c in terms of n we have
# c(1) = 1, c(3) = 9, c(5) = 25
# so c(n) = n^2

# Thus the total for the layer of size n is 4 * n^2 + 10 * (n - 1)

# Thus the sum for the layers up to n is the sum of this quantity over odd n
# The sum of quadratics like this will yield a cubic
# So we can either just write a loop to find the sum
# Or find the cubic that fits the first 4 points

# The first 4 layer sums are
# L(1) = 1
# L(3) = 4 * 1 + 10 * 2 = 24
# L(5) = 4 * 9 + 10 * 4 = 76
# L(7) = 4 * 25 + 10 * 6 = 160

# So the first 4 total sums are
# S(1) = 1
# S(3) = S(1) + 24 = 25
# S(5) = S(3) + 76 = 101
# S(7) = S(5) + 160 = 261

# Fitting the coefficients of the corresponding cubic is just linear algebra, and gives
# S(n) = (2 / 3) * n ^ 3 + (1 / 2) n ^ 2 + 4 * n / 3 - 3 / 2

def spiral_diagonal_sum(n):
    return (4 * (n ** 3) + 3 * (n ** 2) + 8 * n - 9) // 6

print(spiral_diagonal_sum(1001))