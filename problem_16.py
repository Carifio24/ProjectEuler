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

# For extracting digits
# Assume the number is three digits at most
def get_digits(n):
    ones = n % 10
    tens = (n - ones) // 10
    return [ones, tens]

def propagate_carries(digits):
    for d in range(len(digits)-1):
        if digits[d] > 9:
            ones, tens = get_digits(digits[d])
            digits[d] = ones
            digits[d+1] += tens

# Now, we multiply
# We use the fact that every number is at most 100
# This tells us that we can't get carries more than 2 places away
# i.e. 9 * 100 = 900 - we don't need to worry about the thousands place, which would be three places away from our digit of 9
power = 1000
for i in range(power-1):
    digits = [ x * 2 for x in digits ]
    propagate_carries(digits)

print(sum(digits))
