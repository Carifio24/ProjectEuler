####################################################
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
####################################################

collatz_lengths = { 1 : 1 }

# Generate the Collatz sequence for a given number
# To avoid repeated computation, we store pre-computed results
# We start with just the obvious result that 1 gives a length-1 sequence
def collatz_length(n):
    global collatz_lengths

    # If we've already done this one
    if n in collatz_lengths.keys():
        return collatz_lengths[n]

    # Otherwise, we update the number and recurse
    if n % 2 == 0:
        m = n // 2
    else:
        m = 3 * n + 1
    length = 1 + collatz_length(m)
    collatz_lengths[n] = length
    return length

# Perform the calculation for all values up to 1 million
# We store the results in our dictionary
for n in range(2, 1000000):
    _ = collatz_length(n)

# Sort the results
collatz_lengths = sorted(collatz_lengths.items(), key=lambda x: x[1], reverse=True)

# Our answer is the first key
print(collatz_lengths[0][0])