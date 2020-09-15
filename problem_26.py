####################################################
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
####################################################

# There are two parts to this problem:
# 1) When does a fraction have a recurring part?
# 2) If it has one, how long will that recurring part be?

# Part 1 is easy: a fraction written in simplest form as m/n has a recurring part when n has a prime divisor that the base doesn't
# We're in base 10, so that means that n has a prime factor that isn't 2 or 5

# Part 2 is harder, but we can solve it using modular arithmetic
# To do this, let's think about what a digit in a decimal representation really means
# If a number has i as the nth digit after the decimal point, we're saying that we get a contribution of i/10^n
# Since a decimal representation is really a way of writing a number as ... + a * 10^2 + b * 10 + c + d * 10^(-1) + e * 10^(-2) + ...

# We're only considering values of the form 1/n for n > 1, so 1/n < 1
# Suppose we have 1/n = a1 * 10^(-1) + a2 * 10^(-2) + ... + an * 10^(-n) + ...
# Note that ai >= 0 for each i
# We can extract the ith digit ai using modular arithmetic as ai = floor(10^i / n) mod 10
# For example, if i = 2, 100/n = a1 * 10 + a2 + a3, so floor(100/n) = a1 * 10 + a2, which is equal to a2 mod 10

# Using this, we can determine the length of the recurring part of the fraction
# Proposition: The length of the recurring part of the fraction is equal to the order of 10 modulo n
# Proof: First, we note that the a_{i+1} is determined by n and a_{i}
# To see this, note that a_{i+1} = floor(10 * [(10^i/n) - a1])
# Thus, once we find the smallest i, j with i < j such that aj == ai, we find the length of our recurring part
# as j - i

# Next, suppose 10^j = 10^i (mod n) for i != j
# WLOG, we can take i < j
# This means there exists an integer k > 0 such that 10^j - 10^i = nk
# Using the identity x mod y = x - y * floor(x/y), we can write
# 10^i = 10^i mod n + n * floor(10^i/n)
# 10^j = 10^j mod n + n * floor(10^j/n)
# Combining this with the above yields
# nk = (10^j-10^i) mod n + n * (floor(10^j/n) - floor(10^i/n))

