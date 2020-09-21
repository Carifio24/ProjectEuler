####################################################
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
####################################################

# If we have an integer k and a sequence of numbers (1, 2, ..., n)
# the number that we get from concatenating the products is
# k + 10 * 2k + 10^(ND(k) + ND(2k)) * 3k + 10^(ND(k) + ND(2k) + ND(3k)) + ...
# where ND(x) = floor(log10(x)) + 1 is the number of digits in x
# and obviously 

# This is pretty messy, so maybe it's better to work bottom-up
# For each number, we just keep going (i.e. adding to our list 1, 2, ...) until the result has a repeated digit, or exceeds the maximum pandigital number, 987654321
# Obviously, if the number itself has repeated digits, it's a non-starter

from euler import digits, num_digits

# Is a number pandigital or not?
def is_pandigital(x):
    return sorted(digits(x)) == list(range(1,10))

def has_repeated_digit(n):
    dgts = digits(n)
    return len(dgts) > len(set(dgts))

for n in range(2, 987654321 // 2):
    
    x = 1
    val = n
    while (not has_repeated_digit(val)) and val < 987654321:

