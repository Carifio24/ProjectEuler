####################################################
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
####################################################

# How high can these go?
# The largest digit factorial is 9! = 362880
# An n-digit number x lies in the range 10^(n-1) <= x < 10^n
# The maximum factorial sum for an n-digit number is n * 9!
# so once n * 9! < 10^(n-1), we're done
# We have equality at
# n - 1 = log10(n * 9!) = log10(n) + log10(9!)
# which has a solution of 7.43...
# so we only need to consider up to 7-digit numbers

from euler import digits

factorials = {}
def factorial(n):
    global factorials

    if n in factorials.keys():
        return factorials[n]

    if n == 0 or n == 1:
        factorials[n] = 1
        return 1
    r = n * factorial(n-1)
    factorials[n] = r
    return r

digit_factorials = [ factorial(x) for x in range(0, 10) ]
total = 0
for n in range(10, 10**7):
    dgs = digits(n)
    fac_sum = sum(digit_factorials[d] for d in dgs)
    if fac_sum == n:
        total += n

print(total)