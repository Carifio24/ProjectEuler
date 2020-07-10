# ####################################################
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
####################################################

# As always with these problems, the trick is to get the digits without having to explicitly compute the number
# Putting it into Google shows that 100! is around 10^157, so we probably could just do it
# But that's not really any fun

# Without the magic power of Google, roughly how many digits does 100! have?
# We know that 100! < 100^100 (there are 100 factors in 100!, all but one of which are less than 100)
# 100^100 = (10^2)^100 = 10^200
# So with basically no effort, we can say that 100! has < 200 digits
# 200 isn't that large, so we can just live with that

# This is just a slightly-improved version of what I did for problem 16

# For extracting digits
# Assume the number is three digits at most
def get_digits(n):
    ones = n % 10
    tens = ((n - ones) % 100) // 10
    hundreds = (n - ones - tens) // 100
    return [ones, tens, hundreds]

def propagate_carries(digits):
    for d in range(len(digits)):
        if digits[d] > 9:
            ones, tens, hundreds = get_digits(digits[d])
            digits[d] = ones
            digits[d+1] += tens
            digits[d+2] += hundreds

# Our digits - definitely more than we'll need (see above discussion)
# We start our value at 1
digits = [ 1 ] + [ 0 for i in range(199) ]

# Now, we multiply
# We use the fact that every number is at most 100
# This tells us that we can't get carries more than 2 places away
# i.e. 9 * 100 = 900 - we don't need to worry about the thousands place, which would be three places away from our digit of 9
factorial = 100
for i in range(2, factorial+1):
    digits = [ x * i for x in digits ]
    propagate_carries(digits)

print(sum(digits))