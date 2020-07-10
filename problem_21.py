# ####################################################
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
####################################################

from euler import factors

divisor_sums = {}
max_value = 10000

for i in range(2,max_value):
    divisor_sums[i] = int(sum(factors(i)) - i)

amicable_numbers = set()
for i in range(2, max_value):
    j = divisor_sums[i]

    # If we've already found this value from its partner
    if i in amicable_numbers:
        continue

    if j not in divisor_sums.keys():
        divisor_sums[j] = int(sum(factors(j)) - j)

    if divisor_sums[j] == i and i != j:
        if j > 0 and j < max_value:
            amicable_numbers.add(j)
        if i > 0 and i < max_value:
            amicable_numbers.add(i)

print(sum(amicable_numbers))
