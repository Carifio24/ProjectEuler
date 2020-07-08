####################################################
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
####################################################


# For a r x c grid (r rows, c columns), Let f(r,c) denote the number of possible paths
# I have two initial moves: down, or right
# Since I can't move left or up, if I initially move right, I now have f(r, c-1) remaining possible paths to take
# Similarly, if the first move is down, there are f(r-1, c) possible paths
# So I get a recurrence relation f(r,c) = f(r-1, c) + f(r, c-1)
# Also, note that f is symmetric: f(r,c) = f(c,r)
# The base cases are f(n,1) = f(1,n) = n + 1 (how many times to go down/right to start)

# To avoid doing redundant calculations, we cache answers

# Note: f(2,n) is a triangular number. Based on this and the recurrence relation, there should be some formula
# for f(m,n) in terms of 3, 4, ... max(m+1,n+1)-agonal numbers that isn't worth the time to figure out

cached_results = {}

# We assume r, c >= 1
def paths_count(r,c):
    global cached_results

    # Since the function is symmetric, then WLOG it's fine to make r <= c
    r, c = sorted((r,c))

    if (r,c) in cached_results:
        return cached_results[(r,c)]

    if r == 1:
        return c + 1
    else:
        value = paths_count(r-1,c) + paths_count(r,c-1)
        cached_results[(r,c)] = value
        return value


# Print the result
print(paths_count(20,20))