####################################################
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
####################################################

# Solving this requires extracting the digits of 2^1000.
# Obviously the key is to get the digits without just brute-force computing the number

# First off, how many digits does 2^1000 have?
# This is given by the ceiling of log_10(2^1000)
# log_10(2^1000) = 1000 * log_10(2) = 301.03, so there are 302 digits

# The key is to do the multiplication digit-by-digit at each step

# Start off with the digits as all zeros, except for the ones digit
n_digits = 303
digits = [ 0 for i in range(n_digits) ]
digits[0] = 2

# Do the loop
# To save computations at each iteration, keep track of how many digits we have
power = 1
max_populated_digit = 0
while power < 1000:
    for i in range(max_populated_digit+1):
        new_digit = 2 * digits[i]
        if new_digit >= 10:
            new_digit = new_digit - 10
            digits[i+1] += 1
            if i == max_populated_digit:
                max_populated_digit += 1
        digits[i] = new_digit
    power += 1

print(sum(digits))
