####################################################
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
####################################################

# My first observation is that if I start at any given point, the possible paths from that point form a new triangle with that point as the tip
# So the max path from a given node is the node value plus the maximum of the best path from the left node and the best path from the right node
# i.e. max_path_val = node_value + max(left_max_path_val, right_max_path_val)
# Thus we can just work up from the bottom
# Also note that node i in a given row connects to nodes i, i+1 in the row below

# The triangle
triangle_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Split the triangle into rows
rows = triangle_str.split('\n')
n_rows = len(rows)

# Parse the rows and create the triangle
triangle = [ [int(x) for x in row.split()] for row in rows ]

# A container for storing the max path values
max_path_values = [ [ 0 for x in row ] for row in triangle ]

# The max path values for the bottom row are just those values
bottom_row = n_rows-1
for c in range(len(triangle[bottom_row])):
    max_path_values[bottom_row][c] = triangle[bottom_row][c]

# Now we work from the bottom up, finding the max path for each
for r in range(n_rows-2, -1, -1):
    for c in range(len(triangle[r])):
        max_path_values[r][c] = triangle[r][c] + max(max_path_values[r+1][c], max_path_values[r+1][c+1])

# The max for the entire triangle is the max from the top node
print(max_path_values[0][0])