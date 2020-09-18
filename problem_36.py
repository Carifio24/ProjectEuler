####################################################
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)
####################################################

from euler import digits

def is_palindromic(lst):
    """Returns True if the given list is a palindrome; False otherwise."""
    return all( lst[i] == lst[-(i+1)] for i in range(len(lst)) )


total = 0
for n in range(1, 1000000):
    dgs2 = digits(n, 2)
    if not is_palindromic(dgs2):
        continue
    dgs10 = digits(n) # Base 10 is default
    if is_palindromic(dgs10):
        total += n

print(total)