# ARC Task 025

def mostcolor(grid):
    values = [v for r in grid for v in r]
    return max(set(values), key = values.count)


def height(piece):
    if len(piece) == 0:
        return 0
    return lowermost(piece) - uppermost(piece) + 1


def width(piece):
    if len(piece) == 0:
        return 0
    return rightmost(piece) - leftmost(piece) + 1


def toindices(patch):
    if len(patch) == 0:
        return set()
    first = next(iter(patch))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        obj = patch
        return {index for _, index in obj}
    return patch


def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    first = next(iter(patch))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        obj = patch
        return {(value, (i + di, j + dj)) for value, (i, j) in obj}
    idx = patch
    return {(i + di, j + dj) for i, j in idx}


def objects(grid, univalued, diagonal, without_bg):
    bg = mostcolor(grid) if without_bg else None
    objs = []
    occupied = set()
    h, w = (len(grid), len(grid[0]))

    unvisited = {(i, j) for i in range(h) for j in range(w)}

    def neighbors(loc):
        i, j = loc
        if diagonal:
        return {
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
        }
        return {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}

    for loc in unvisited:
        if loc in occupied:
        continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
        continue
        obj = {(val, loc)}
        cands = {loc}
        while cands:
        neighborhood = set()
        for cand in cands:
        v = grid[cand[0]][cand[1]]
        if val == v if univalued else v != bg:
        obj.add((v, cand))
        occupied.add(cand)
        neighborhood |= {
        (i, j) for (i, j) in neighbors(cand) if 0 <= i < h and 0 <= j < w
        }
        cands = neighborhood - occupied
        objs.append(obj)
    return objs


def uppermost(patch):
    return min((i for i, j in toindices(patch)))


def lowermost(patch):
    return max((i for i, j in toindices(patch)))


def leftmost(patch):
    return min((j for i, j in toindices(patch)))


def rightmost(patch):
    return max((j for i, j in toindices(patch)))


def center(patch):
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)


def gravitate(source, destination):
    si, sj = center(source)
    di, dj = center(destination)
    i, j = (0, 0)
    cols_s = set(j for _, j in toindices(source))
    cols_d = set(j for _, j in toindices(destination))
    if cols_s & cols_d:
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    gi, gj = (i, j)
    c = 0

    def _adj(a, b):
        ia, ib = toindices(a), toindices(b)
        return min(abs(ai - bi) + abs(aj - bj) for ai, aj in ia for bi, bj in ib) == 1

    while not _adj(source, destination) and c < 42:
        c += 1
        gi += i
        gj += j
        source = shift(source, (i, j))
    return (gi - i, gj - j)


def solve_1a07d186(I):
    objs = objects(I, True, False, True)

    groups = {}
    for o in objs:
        groups.setdefault(next(iter(o))[0], []).append(o)

    moved = []
    to_remove = []
    for c, arr in groups.items():
        if not arr:
        continue

        non_single = [o for o in arr if len(o) >= 2]

        H, W = len(I), len(I[0])

        def large_enough(o):
        oh, ow = height(o), width(o)

        is_hline = ow == len(o) and oh == 1
        is_vline = oh == len(o) and ow == 1
        if is_hline:
        return ow >= (W // 2)
        if is_vline:
        return oh >= (H // 2)
        return len(o) >= max(H, W) // 2

        big_enough = [o for o in non_single if large_enough(o)]

        border_candidates = [
        o
        for o in big_enough
        if (
        uppermost(o) == 0
        or leftmost(o) == 0
        or lowermost(o) == H - 1
        or rightmost(o) == W - 1
        )
        ]
        if border_candidates:
        anchor = max(border_candidates, key = lambda o: len(o))
        elif big_enough:
        anchor = max(big_enough, key = lambda o: len(o))
        else:
        anchor = None
        if anchor is None:
        to_remove.extend(arr)
        continue

        for o in arr:
        if o is anchor:
        continue
        if len(o) == 1:
        rows_o = {i for i, _ in toindices(o)}
        rows_a = {i for i, _ in toindices(anchor)}
        cols_o = {j for _, j in toindices(o)}
        cols_a = {j for _, j in toindices(anchor)}
        aligned = (rows_o & rows_a) or (cols_o & cols_a)
        if not aligned:
        to_remove.append(o)
        continue
        off = gravitate(o, anchor)
        moved.append(shift(o, off))
        to_remove.append(o)

    g = [list(r) for r in I]
    if to_remove:
        mc = mostcolor(I)
        for o in to_remove:
        for i, j in toindices(o):
        g[i][j] = mc
    for o in moved:
        for v, (i, j) in o:
        g[i][j] = v
    return g


def p(g):
    return solve_1a07d186(g)
