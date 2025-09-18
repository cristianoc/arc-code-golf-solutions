# ARC Task 392

ZERO, ONE, FIVE = 0, 1, 5

def _least_color(I):
    from collections import Counter
    c = Counter(v for r in I for v in r)
    return min(c, key = c.get)

def _components(I):
    h, w = len(I), len(I[0])
    seen = [[False]*w for _ in range(h)]
    comps = []  # list of (color, set of (i, j))
    for i in range(h):
        for j in range(w):
        if seen[i][j]:
        continue
        col = I[i][j]
        q = [(i, j)]
        seen[i][j] = True
        cells = []
        while q:
        x, y = q.pop()
        cells.append((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and I[nx][ny]==col:
        seen[nx][ny]=True
        q.append((nx, ny))
        comps.append((col, set(cells)))
    return comps

def _bbox(cells):
    is_ = [i for i, _ in cells]
    js_ = [j for _, j in cells]
    return min(is_), max(is_), min(js_), max(js_)

def _outbox(cells):
    if not cells:
        return set()
    r1, r2, c1, c2 = _bbox(cells)
    r1-=1
    r2+=1
    c1-=1
    c2+=1
    box = set()
    for j in range(c1, c2 + 1):
        box.add((r1, j))
        box.add((r2, j))
    for i in range(r1, r2 + 1):
        box.add((i, c1))
        box.add((i, c2))
    return box

def _fill(I, val, cells):
    h, w = len(I), len(I[0])
    O = [list(r) for r in I]
    for i, j in cells:
        if 0<=i<h and 0<=j<w:
        O[i][j]=val
    return tuple(tuple(r) for r in O)

def solve_f8c80d96(I):
    comps = _components(I)
    lc = _least_color(I)
    # largest component of least color
    lc_comps = [cells for col, cells in comps if col==lc]
    base = max(lc_comps, key = len)
    # smallest width among all components
    def comp_width(cs):
        r1, r2, c1, c2 = _bbox(cs)
        return c2 - c1 + 1
    minw_cells = min((cells for _, cells in comps), key = comp_width)
    start_with_outbox = (len(minw_cells) != ONE)

    def add_rings(cells, inc):
        cur = set(cells)
        for _ in range(inc):
        cur = _outbox(cur)
        return cur

    inc = 2 + (1 if start_with_outbox else 0)
    r1 = add_rings(base, inc)
    r2 = add_rings(r1, inc)
    r3 = add_rings(r2, inc)

    G = _fill(I, lc, r1)
    G = _fill(G, lc, r2)
    G = _fill(G, lc, r3)
    # replace zeros with FIVE
    O = tuple(tuple(FIVE if v==ZERO else v for v in row) for row in G)
    return O

def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_f8c80d96(G)
    return [list(r) for r in R]
