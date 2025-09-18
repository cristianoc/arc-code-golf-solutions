# ARC Task 148

F = False
T = True

ZERO = 0
ONE = 1
TWO = 2
FOUR = 4
EIGHT = 8

def _bg_color(G):
    flat = [v for r in G for v in r]
    return max(set(flat), key = flat.count)

def _components_of_color(G, color):
    h, w = len(G), len(G[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
        if G[i][j] != color or seen[i][j]:
        continue
        q = [(i, j)]
        seen[i][j] = True
        cur = []
        while q:
        a, b = q.pop()
        cur.append((a, b))
        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        na, nb = a + da, b + db
        if 0<=na<h and 0<=nb<w and not seen[na][nb] and G[na][nb]==color:
        seen[na][nb]=True
        q.append((na, nb))
        comps.append(cur)
    return comps

def solve_673ef223(I):
    h, w = len(I), len(I[0])
    bg = _bg_color(I)

    # Record original 8s and make a base grid with 8->4
    eights = [(i, j) for i in range(h) for j in range(w) if I[i][j]==EIGHT]
    O = [list(row) for row in I]
    for i, j in eights:
        O[i][j] = FOUR

    # Helper to fill a cell if it is background
    def underfill_cell(i, j):
        if 0<=i<h and 0<=j<w and O[i][j]==bg:
        O[i][j]=EIGHT

    # For each 8, connect horizontally to nearest 2 in the row and underfill along the span
    for i, j in eights:
        left = None
        for k in range(j - 1, -1, -1):
        if I[i][k]==TWO:
        left = k
        break
        right = None
        for k in range(j + 1, w):
        if I[i][k]==TWO:
        right = k
        break
        target = None
        if left is not None and right is not None:
        target = left if (j - left) <= (right - j) else right
        else:
        target = left if left is not None else right
        if target is not None:
        a, b = min(j, target), max(j, target)
        for x in range(a, b + 1):
        underfill_cell(i, x)

    # Compute vertical offset from top rows of 2 - components
    comps2 = _components_of_color(I, TWO)
    if comps2:
        tops = [min(i for i, _ in comp) for comp in comps2]
        di = max(tops) - min(tops)
    else:
        di = 0

    # For each 8 shifted down by di, fill its entire row on background cells
    for i, j in eights:
        ni = i + di
        if 0 <= ni < h:
        for jj in range(w):
        underfill_cell(ni, jj)

    return tuple(tuple(row) for row in O)

def p(g):
    I = tuple(tuple(r) for r in g)
    R = solve_673ef223(I)
    return [list(r) for r in R]
