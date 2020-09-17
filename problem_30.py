####################################################
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
####################################################

# The largest digit to a 5th power is 9^5 = 59,049
# Thus the maximum number of digits n that we need to consider is when log10(n * 9^5) < n - 1
# as an n-digit number x has log10(x) >= n - 1
# so this inequality tells us when the sum of the digits cannot exceed the value

# This inequality has a solution at n = 6.59...
# So we only need to consider 6-digit numbers, i.e. up to 999999

from euler import digits

total = 0
digit_powers = [ x ** 5 for x in range(10) ]
for i in range(2, 1000000):
    dgs = digits(i)
    s = sum(digit_powers[i] for i in dgs)
    if s == i:
        total += i

print(total)