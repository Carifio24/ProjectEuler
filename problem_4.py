####################################################
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
####################################################

from math import floor, sqrt

# Check whether or not a number is a palindrome
def is_palindrome(n):
    n_str = str(n)
    n_digits = len(n_str)
    for i in range(n_digits // 2):
        if n_str[i] != n_str[n_digits-1-i]:
            return False
    return True

# Check whether a number is a product of three-digit numbers
def factor_condition(x):
    for i in range(100, min(1000, floor(sqrt(x)))):
        if (x % i == 0):
            q = x / i
            if q >= 100 and q < 1000:
                return True
    return False

# The upper bound of the scan range is 999 * 999 = 998001
# So work backwards from there
num = 998001
while True:
    num -= 1
    if not (is_palindrome(num) and factor_condition(num)):
        continue
    break


print(num)