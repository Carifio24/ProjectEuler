####################################################
# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
####################################################

# We could just run a loop and compute the whole sequence until we get to 1000 digits, but that's boring

# It might be fruitful to use the closed form here
# Which is Fn = ((phi)^n - (1-phi)^n) / sqrt(5)

# The condition that Fn has 1000 digits is equivalent to saying that log10(Fn) >= 999
# Again, we could just put this inequality into some solver, but that's also no fun
# Let's see what we can do ourselves

# From the above, we get
# log10(Fn) = log10(phi^n - (1-phi)^n) - (1/2) * log10(5)

# With some log algebra, we can rewrite this as
# log10(Fn) = n * log10(phi) + log10(1 - (1/phi - 1)^n) - (1/2) * log10(5)

# Note that (1/phi - 1) = -0.382, so the term inside the second log will quickly go to 1 as n -> infinity
# so the log will quickly go to zero
# For example, by n=10 it's already down to -0.0000287

# So we can ignore that term, and approximate log10(Fn) = n * log10(phi) - (1/2) * log10(5)
# So now we're just solving n * log10(phi) - (1/2) * log10(5) >= 999
# or n >= (999 + (1/2) * log10(5)) / log10(phi)

from math import ceil, log10, sqrt

power_of_10 = 999
phi = (1 + sqrt(5)) / 2

print(ceil( (power_of_10 + 0.5 * log10(5) ) / log10(phi) ))