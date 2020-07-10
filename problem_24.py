####################################################
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
####################################################

# We have 10 digits
# Once I choose the first digit, there are 9! possible permutations that start with that digit
# 9! = 362,880
# 1,000,000 / 362,880 = 2.756
# So the millionth permutation will start with 2 (the third digit in order)
# and will be the 1,000,000 - 2 * 362,880 = 274,240th permutation starting with 2

# Now to the second digit
# Once the second digit is picked, there are 8! = 40,320 permutations with that second digit
# and so on

from math import factorial

# The set of digits
digits = [ n for n in range(10) ]

perm_index = 1000000 - 1  # Zero indexing means that the millionth permutation is at index 999,999

# Container for storing the result
permutation_digits = []

# While we have digits left to choose from, repeat the process described above
# Find the next digit in order that we want, decrease the index appropriately, and remove the chosen digit from future consideration
while len(digits) > 0:
    fac = factorial(len(digits)-1)
    next_digit_index = perm_index // fac
    next_digit = digits[next_digit_index]
    perm_index -= next_digit_index * fac

    digits.remove(next_digit)
    permutation_digits.append(next_digit)

print(''.join([str(x) for x in permutation_digits]))