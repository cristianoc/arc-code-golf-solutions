# Simplified helpers; prefer sets/lists over frozenset
def mostcolor(element):
    # Grids: list/tuple of rows; objects: set of (v,(i,j))
    values = [v for r in element for v in r] if isinstance(element, (tuple, list)) else [t[0] for t in element]
    return max(set(values), key=values.count)
def neighbors(loc):
    # 8-neighborhood (including diagonals)
    i, j = loc
    return {
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1),                 (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
    }
def asindices(grid):
    if not grid or not grid[0]:
        return set()
    return {(i, j) for i in range(len(grid)) for j in range(len(grid[0]))}
def ulcorner(patch):
    idx = toindices(patch)
    return (min((i for i, _ in idx)), min((j for _, j in idx)))
def lrcorner(patch):
    idx = toindices(patch)
    return (max((i for i, _ in idx)), max((j for _, j in idx)))
def toindices(patch):
    if len(patch) == 0:
        return set()
    first = next(iter(patch))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        return {index for _, index in patch}
    return patch
def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    first = next(iter(patch))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        return {(value, (i + di, j + dj)) for value, (i, j) in patch}
    return {(i + di, j + dj) for i, j in patch}
def normalize(patch):
    if len(patch) == 0:
        return patch
    return shift(patch, (-uppermost(patch), -leftmost(patch)))
def dneighbors(loc):
    return {(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)}
def objects(grid, univalued, diagonal, without_bg):
    bg = mostcolor(grid) if without_bg else None
    objs = []
    occupied = set()
    h, w = (len(grid), len(grid[0]))
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
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
                if (val == v) if univalued else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
            cands = neighborhood - occupied
        objs.append(obj)
    return objs
def fgpartition(grid):
    bg = mostcolor(grid)
    return [
        {(v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value}
        for value in (palette(grid) - {bg})
    ]
def uppermost(patch):
    return min((i for i, j in toindices(patch)))
def leftmost(patch):
    return min((j for i, j in toindices(patch)))
def rightmost(patch):
    return max((j for i, j in toindices(patch)))
def manhattan(a, b):
    return min((abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b)))
def palette(element):
    if isinstance(element, (tuple, list)):
        return {v for r in element for v in r}
    return {t[0] for t in element}
def rot90(grid):
    # Accept tuple or list grid; return list-of-lists
    return [list(row) for row in zip(*grid[::-1])]
def hmirror(piece):
    # Mirror an object or index-set across the horizontal axis
    d = ulcorner(piece)[0] + lrcorner(piece)[0]
    first = next(iter(piece))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        return {(v, (d - i, j)) for v, (i, j) in piece}
    return {(d - i, j) for i, j in piece}
def vmirror(piece):
    # Mirror an object or index-set across the vertical axis
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    first = next(iter(piece))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        return {(v, (i, d - j)) for v, (i, j) in piece}
    return {(i, d - j) for i, j in piece}
def dmirror(piece):
    # Mirror across the main diagonal for objects or index-sets
    a, b = ulcorner(piece)
    first = next(iter(piece))
    if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
        return {(v, (j - b + a, i - a + b)) for v, (i, j) in piece}
    return {(j - b + a, i - a + b) for i, j in piece}
def cmirror(piece):
    # Mirror across the counter-diagonal for objects or index-sets
    return vmirror(dmirror(vmirror(piece)))
def paint(grid, obj):
    h, w = (len(grid), len(grid[0]))
    grid_painted = [list(row) for row in grid]
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return grid_painted
def canvas(value, dimensions):
    # Create list-of-lists canvas
    return [[value for _ in range(dimensions[1])] for _ in range(dimensions[0])]
# (Unused gravitate removed)
def solve_4290ef0e(I):
    # Normalize input grid type
    if not isinstance(I, tuple):
        I = tuple(tuple(row) for row in I)

    bg = mostcolor(I)

    # Areas by foreground color and connected components for scoring
    areas = fgpartition(I)
    comps = objects(I, True, False, True)

    # Scoring key: -( 2*max(width) + adjusted min pairwise manhattan )
    def score_key(area):
        # Inline color/colorfilter and width
        c = next(iter(area))[0]
        comps_c = [obj for obj in comps if next(iter(obj))[0] == c]
        if comps_c:
            max_w = max((rightmost(x) - leftmost(x) + 1 for x in comps_c), default=0)
        else:
            max_w = 0
        dists = {manhattan(i, j) for j in comps_c for i in comps_c}
        dists_nz = {d for d in dists if d != 0}
        mind = min(dists_nz, default=0)
        d_term = (mind - 1) if mind > 0 else -2
        return -(2 * max_w + d_term)

    # Order areas by the scoring key
    ordered_areas = sorted(areas, key=score_key)

    # Reflect each area: choose orientation by minimizing the sum of the
    # normalized center-of-mass coordinates. This tends to favor placements
    # that are closest to the top-left after normalization and, under ties,
    # prefers diagonal mirroring due to candidate order.
    def orient(area):
        # Canonicalize orientation by lexicographically minimizing the
        # normalized index set. This yields a stable representative across
        # mirror-equivalent variants and matches expected symmetries.
        def canon_key(piece):
            return tuple(sorted(toindices(normalize(piece))))

        cands = (vmirror(area), dmirror(area), cmirror(area), hmirror(area))
        return min(cands, key=canon_key)

    reflected = [orient(area) for area in ordered_areas]

    # Normalize pieces to origin
    norm_pieces = tuple(normalize(x) for x in reflected)

    # Determine k per original rule
    num_colors = len(areas)
    k = num_colors if any(len(a) == 1 for a in areas) else (num_colors + 1)

    # Place pieces at diagonal offsets and compose onto 4 rotations
    offsets = tuple((i, i) for i in range(k))
    placed = tuple(
        p for piece, off in zip(norm_pieces, offsets)
        for p in sorted(shift(piece, off), key=lambda t: t[1])
    )
    size_dim = 2 * k - 1
    out = canvas(bg, (size_dim, size_dim))
    for _ in range(3):
        out = paint(out, placed)
        out = rot90(out)
    out = paint(out, placed)
    return out
def p(g):
    return solve_4290ef0e(g)
