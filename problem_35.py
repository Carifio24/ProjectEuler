####################################################
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?
####################################################

from euler import digits, from_digits, is_prime


def digit_rotations(n):
    """Get all of the rotations of a number."""
    dgs = digits(n)
    digit_sets = [ dgs[-i:] + dgs[:-i] for i in range(len(dgs)) ]
    return [ from_digits(x) for x in digit_sets ]


# Find all the primes below one million
primes = set( x for x in range(2, 1000000) if is_prime(x) )

# Count the number of circular primes
circular_primes = set()
for p in primes:

    # If we've already gotten this prime from one of its rotations, skip it
    if p in circular_primes:
        continue

    # If all of the rotations are prime, add them all to the set
    rots = digit_rotations(p)
    is_cp = all(x in primes for x in rots)
    if is_cp:
        circular_primes.update(rots)

print(len(circular_primes))