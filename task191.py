ZERO = 0
ONE = 1
FOUR = 4

def solve_7df24a62(I):
    G = I
    h, w = len(G), len(G[0])

    def ofcolor(grid, val):
        return {(i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == val}

    def ulcorner(coords):
        mi = min(i for i, _ in coords)
        mj = min(j for _, j in coords)
        return (mi, mj)

    def bbox(coords):
        if not coords:
            return (0, 0, -1, -1)
        r1 = min(i for i, _ in coords)
        r2 = max(i for i, _ in coords)
        c1 = min(j for _, j in coords)
        c2 = max(j for _, j in coords)
        return r1, c1, r2, c2

    def rot90(grid):
        return tuple(tuple(row) for row in zip(*grid[::-1]))

    def rot180(grid):
        return tuple(tuple(row[::-1]) for row in grid[::-1])

    def rot270(grid):
        return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

    def normalize(coords):
        if not coords:
            return set()
        mi, mj = ulcorner(coords)
        return {(i - mi, j - mj) for (i, j) in coords}

    def height_width_from_coords(coords):
        if not coords:
            return (0, 0)
        r1, c1, r2, c2 = bbox(coords)
        return (r2 - r1 + 1, c2 - c1 + 1)

    def fill_with_value(grid, val, coords):
        out = [list(r) for r in grid]
        for i, j in coords:
            if 0 <= i < h and 0 <= j < w:
                out[i][j] = val
        return tuple(tuple(r) for r in out)

    ones_all = ofcolor(G, ONE)
    fours_all = ofcolor(G, FOUR)
    if not ones_all:
        return G

    r1 = min(i for i, _ in ones_all)
    r2 = max(i for i, _ in ones_all)
    c1 = min(j for _, j in ones_all)
    c2 = max(j for _, j in ones_all)
    base_ul = (r1, c1)
    sub = tuple(tuple(G[i][c1:c2+1]) for i in range(r1, r2+1))

    rotations = [sub, rot90(sub), rot180(sub), rot270(sub)]
    # Include mirror variants to capture reflected patterns
    def flip_h(grid):
        return tuple(tuple(row[::-1]) for row in grid)
    rotations += [flip_h(r) for r in rotations]

    to_fill = set()

    for rot in rotations:
        # pattern of 4s and 1s in the rotated subgrid
        p4 = {(i, j) for i, row in enumerate(rot) for j, v in enumerate(row) if v == FOUR}
        p1 = {(i, j) for i, row in enumerate(rot) for j, v in enumerate(row) if v == ONE}

        # base 4s of this rotation positioned at original ones' ulcorner
        base4_global = {(i + base_ul[0], j + base_ul[1]) for (i, j) in p4}
        # Use all 4s for matching to allow windows overlapping the base pattern
        remainder4 = fours_all

        # normalized patterns and relative offset between 1s and 4s in this rotation
        p4_ul = ulcorner(p4) if p4 else (0, 0)
        p1_ul = ulcorner(p1) if p1 else (0, 0)
        dy = p1_ul[0] - p4_ul[0]
        dx = p1_ul[1] - p4_ul[1]
        p4n = normalize(p4)
        p1n = normalize(p1)

        ph, pw = height_width_from_coords(p4n)
        max_i = h - ph + 1
        max_j = w - pw + 1
        if max_i < 0 or max_j < 0:
            continue

        for oi in range(max_i):
            for oj in range(max_j):
                placed4 = {(i + oi, j + oj) for (i, j) in p4n}
                # Prefer exact 4-pattern match within the window
                window4 = {
                    (i, j)
                    for (i, j) in remainder4
                    if oi <= i < oi + ph and oj <= j < oj + pw
                }
                if window4 == placed4:
                    placed1 = {(i + oi + dy, j + oj + dx) for (i, j) in p1n}
                    to_fill.update(placed1)

    O = fill_with_value(G, ONE, to_fill)
    return O

def _to_list_grid(grid):
    if isinstance(grid, tuple):
        return [list(row) for row in grid]
    return grid

def p(g):
    return _to_list_grid(solve_7df24a62(g))
