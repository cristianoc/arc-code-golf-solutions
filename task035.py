# ARC Task 035

EIGHT = 8
ZERO = 0

def solve_1f642eb9(I):
    # Copy input to a mutable grid
    h, w = len(I), len(I[0])
    grid = [row[:] for row in I]

    # Find the bounding box of the cyan rectangle (value 8)
    top, left, bottom, right = h, w, -1, -1
    for i in range(h):
        for j in range(w):
        if grid[i][j] == EIGHT:
        if i < top:
        top = i
        if i > bottom:
        bottom = i
        if j < left:
        left = j
        if j > right:
        right = j

    # If there is no cyan rectangle, return the input unchanged
    if bottom == -1:
        return [row[:] for row in I]

    # For each non - zero, non - cyan cell, paint its color on the aligned
    # border cell of the cyan rectangle (row/column alignment).
    for i in range(h):
        for j in range(w):
        c = grid[i][j]
        if c == ZERO or c == EIGHT:
        continue

        # Column alignment → top or bottom edge
        if left <= j <= right:
        if i < top:
        grid[top][j] = c
        elif i > bottom:
        grid[bottom][j] = c

        # Row alignment → left or right edge
        if top <= i <= bottom:
        if j < left:
        grid[i][left] = c
        elif j > right:
        grid[i][right] = c

    return [row[:] for row in grid]

def p(g):
    return solve_1f642eb9(g)
