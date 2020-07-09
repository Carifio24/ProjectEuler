####################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
####################################################

from euler import is_prime

total = 0
x = 2
while x < 2000000:
    if is_prime(x):
        total += x
    x += 1

print(total)