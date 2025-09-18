# ARC Task 387

ZERO = 0
FIVE = 5

def solve_f35d900a(I):
    h, w = len(I), len(I[0])
    O = [list(row) for row in I]

    pts, colors = [], set()
    for i in range(h):
        for j in range(w):
        v = I[i][j]
        if v != ZERO:
        pts.append((i, j, v))
        colors.add(v)
    if not pts:
        return I

    cols = sorted(colors)
    def other_color(v):
        return cols[0] if len(cols) == 1 or v == cols[1] else cols[1]

    for i, j, v in pts:
        oc = other_color(v)
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w:
        O[ni][nj] = oc

    r1 = min(i for i, _, _ in pts)
    r2 = max(i for i, _, _ in pts)
    c1 = min(j for _, j, _ in pts)
    c2 = max(j for _, j, _ in pts)

    if c2 > c1:
        for j in range(c1 + 1, c2):
        if min(j - c1, c2 - j) % 2 == 0:
        O[r1][j] = FIVE
        O[r2][j] = FIVE

    if r2 > r1:
        for i in range(r1 + 1, r2):
        if min(i - r1, r2 - i) % 2 == 0:
        O[i][c1] = FIVE
        O[i][c2] = FIVE

    return tuple(tuple(r) for r in O)

def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_f35d900a(G)
    return [list(r) for r in R]
