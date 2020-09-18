####################################################
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
####################################################

from euler import is_prime, digits, from_digits

# We are told that there are 11 truncatable primes
N_TRUNCATABLE = 11

# Get the left and right truncations
def left_truncations(dgts):
    return [ from_digits(dgts[i:]) for i in range(len(dgts)) ]

def right_truncations(dgts):
    return [ from_digits(dgts[:i+1]) for i in range(len(dgts)) ]

# Loop over values until we get to 11 primes
n = 10
primes = set([2, 3, 5, 7])
trunc_primes = set()
while len(trunc_primes) < N_TRUNCATABLE:

    # Only need to look at the truncations if the number itself is prime
    if is_prime(n):
        primes.add(n) # Add the number to the set of primes
        dgts = digits(n)
        left_cond = all(x in primes for x in left_truncations(dgts)) # Are all of the left truncations prime?
        if left_cond:
            right_cond = all(x in primes for x in right_truncations(dgts)) # Are all of the right truncations prime?
            if right_cond:
                trunc_primes.add(n)
    
    # Increment the value
    n += 1

# Find the sum
print(sum(trunc_primes))