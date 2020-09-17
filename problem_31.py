####################################################
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
####################################################

# We want to count the number of distinct non-negative integer solutions {n1, ... n8} to
# n1 + 2 * n2 + 5 * n3 + 10 * n4 + 20 * n5 + 50 * n6 + 100 * n7 + 200 * n8 = 200
# or, more generally, the number of solutions to w dot x = y, for some integer vector w (the weights), a value y, and xi >= 0 for all i

# Let's look at the simplest possible case, with one coin, of value x
# We can make y units from x if y % x == 0, i.e. y = x * n for some n

# The next case is two coins, with values x1, x2
# When can we make y from x1 and x2?
# If there exists n1, n2 s.t.
# n1 * x1 + n2 * x2 == y
# This implies that gcd(x1, x2) | y
# But there may be multiple solutions - how many?
# Let 0 <= n2 <= y / x2
# Then we have a solution if (y - n2 * x2) / x1 is an integer
# Do this for each integer n2 in [0, floor(y / x2)]

# This generalizes - just keep peeling off the last term, and loop over the possible n values

def solutions_count(x, y):

    # The base case - one coin type
    if len(x) == 1:
        return 1 if y % x[0] == 0 else 0
    
    # Otherwise, we recurse
    total = 0
    for n in range(0, (y // x[-1]) + 1): # Need to add one to include the floor in the range
        total += solutions_count(x[:-1], y - n * x[-1])
    return total


coin_values = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
value = 200
print(solutions_count(coin_values, value))