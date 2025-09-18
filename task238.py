# ARC Task 238

def _most_color(grid):
    if not grid or not grid[0]:
        return 0
    cnt = {}
    for row in grid:
        for v in row:
        cnt[v] = cnt.get(v, 0) + 1
    return max(cnt, key = cnt.get)


def objects(grid, univalued, diagonal, without_bg):
    if not grid or not grid[0]:
        return []
    H, W = len(grid), len(grid[0])
    bg = _most_color(grid) if without_bg else None
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        dirs += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    occupied, objs = set(), []
    for i in range(H):
        for j in range(W):
        if (i, j) in occupied:
        continue
        v0 = grid[i][j]
        if v0 == bg:
        continue
        comp, stack = set(), [(i, j)]
        while stack:
        x, y = stack.pop()
        if (x, y) in occupied:
        continue
        v = grid[x][y]
        if (univalued and v != v0) or (not univalued and v == bg):
        continue
        occupied.add((x, y))
        comp.add((v, (x, y)))
        for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in occupied:
        stack.append((nx, ny))
        if comp:
        objs.append(comp)
    return objs


def _toindices(obj):
    if not obj:
        return set()
    e = next(iter(obj))
    if isinstance(e, tuple) and len(e) == 2 and isinstance(e[1], tuple):
        return {(i, j) for _, (i, j) in obj}
    return set(obj)


def _bbox_corners(patch):
    idx = _toindices(patch)
    mi = min(i for i, _ in idx)
    mj = min(j for _, j in idx)
    Mi = max(i for i, _ in idx)
    Mj = max(j for _, j in idx)
    return (mi, mj), (Mi, Mj)


def _normalize(obj):
    if not obj:
        return obj
    (mi, mj), _ = _bbox_corners(obj)
    return {(v, (i - mi, j - mj)) for v, (i, j) in obj}


def _shift(patch, d):
    di, dj = d
    if not patch:
        return patch
    e = next(iter(patch))
    if isinstance(e, tuple) and len(e) == 2 and isinstance(e[1], tuple):
        return {(v, (i + di, j + dj)) for v, (i, j) in patch}
    return {(i + di, j + dj) for i, j in patch}


def _crop(grid, start, dims):
    si, sj = start
    hi, hj = dims
    return [row[sj:sj + hj] for row in grid[si:si + hi]]


def _subgrid(patch, grid):
    (mi, mj), (Mi, Mj) = _bbox_corners(patch)
    return _crop(grid, (mi, mj), (Mi - mi + 1, Mj - mj + 1))


def _vmirror(idx):
    # idx is a set of (i, j)
    idx2 = _toindices(idx)
    if not idx2:
        return set()
    (_, mj), (_, Mj) = _bbox_corners(idx2)
    D = mj + Mj
    return {(i, D - j) for i, j in idx2}


def _connect(a, b):
    ai, aj = a
    bi, bj = b
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    if ai == bi:
        return {(ai, j) for j in range(sj, ej + 1)}
    if aj == bj:
        return {(i, aj) for i in range(si, ei + 1)}
    if bi - ai == bj - aj:  # main diagonal
        return {(i, j) for i, j in zip(range(si, ei + 1), range(sj, ej + 1))}
    if bi - ai == aj - bj:  # anti - diagonal
        return {(i, j) for i, j in zip(range(si, ei + 1), range(ej, sj - 1, -1))}
    return set()


def _paint(grid, obj):
    H = len(grid)
    W = len(grid[0]) if H and grid[0] else 0
    out = [list(r) for r in grid]
    for v, (i, j) in obj:
        if 0 <= i < H and 0 <= j < W:
        out[i][j] = v
    return out


def _fill(grid, value, idx):
    H = len(grid)
    W = len(grid[0]) if H and grid[0] else 0
    out = [list(r) for r in grid]
    for i, j in _toindices(idx):
        if 0 <= i < H and 0 <= j < W:
        out[i][j] = value
    return out


def _numcolors(obj):
    return len({v for v, _ in obj})


def solve_9aec4887(I):
    # Expect and return list - of - lists grids
    comps = objects(I, univalued = False, diagonal = True, without_bg = True)
    if not comps:
        return I

    eight_cells = {(8, (i, j)) for i, row in enumerate(I) for j, v in enumerate(row) if v == 8}

    size = lambda o: len(_toindices(o))
    ref = eight_cells or min(comps, key = _numcolors)

    tgt_candidates = [c for c in comps if {v for v, _ in c} != {8}] or comps
    tgt = max(tgt_candidates, key = size, default = None)
    if not tgt:
        return I

    # Crop using non - 8 frame to avoid oversized bbox.
    frame = {(v, loc) for v, loc in tgt if v != 8}
    cropped = _subgrid(frame or tgt, I)

    ref_idx = _toindices(_shift(_normalize(ref), (1, 1)))
    norm_tgt = list(_normalize(frame or tgt))

    # Paint each ref index with nearest color from normalized target.
    painted = _paint(
        cropped,
        [
        ((min(norm_tgt, key = lambda t, i = i, j = j: abs(t[1][0] - i) + abs(t[1][1] - j))[0]) if norm_tgt else 0,
        (i, j))
        for i, j in ref_idx
        ],
    )

    # Intersect ref with both diagonals of its bbox.
    (a, b), (c, d) = _bbox_corners(ref_idx)
    main = _connect((a, b), (c, d))
    diag_hits = ref_idx & (main | _vmirror(main))
    return _fill(painted, 8, diag_hits)


def p(g):
    return solve_9aec4887(g)
