# ARC Task 280

TWO, THREE = 2, 3

def _mostcolor(grid):
    counts = {}
    for row in grid:
        for v in row:
        counts[v] = counts.get(v, 0) + 1
    return max(counts, key = counts.get)

def _objects(grid):
    h, w = len(grid), len(grid[0])
    bg = _mostcolor(grid)
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
        if seen[i][j] or grid[i][j] == bg:
        continue
        q = [(i, j)]
        seen[i][j] = True
        cur = []  # (val, (i, j))
        while q:
        ci, cj = q.pop()
        v = grid[ci][cj]
        cur.append((v, (ci, cj)))
        for ni, nj in ((ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)):
        if 0 <= ni < h and 0 <= nj < w and not seen[ni][nj] and grid[ni][nj] != bg:
        seen[ni][nj] = True
        q.append((ni, nj))
        comps.append(cur)
    return comps

def _to_indices(patch):
    if not patch:
        return []
    sample = next(iter(patch))
    if isinstance(sample, tuple) and len(sample) == 2 and isinstance(sample[1], tuple):
        return [idx for _, idx in patch]
    return list(patch)

def _bbox_stats(patch):
    idx = _to_indices(patch)
    is_ = [i for i, _ in idx]
    js_ = [j for _, j in idx]
    return min(is_), max(is_), min(js_), max(js_)

def _height(patch):
    if not patch:
        return 0
    mn_i, mx_i, _, _ = _bbox_stats(patch)
    return mx_i - mn_i + 1

def _width(patch):
    if not patch:
        return 0
    _, _, mn_j, mx_j = _bbox_stats(patch)
    return mx_j - mn_j + 1

def _uppermost(patch):
    mn_i, _, _, _ = _bbox_stats(patch)
    return mn_i

def _lowermost(patch):
    _, mx_i, _, _ = _bbox_stats(patch)
    return mx_i

def _leftmost(patch):
    _, _, mn_j, _ = _bbox_stats(patch)
    return mn_j

def _rightmost(patch):
    _, _, _, mx_j = _bbox_stats(patch)
    return mx_j

def _vline(patch):
    idx = _to_indices(patch)
    if not idx:
        return False
    return _width(idx) == 1 and _height(idx) == len(idx)

def _connect(a, b):
    ai, aj = a
    bi, bj = b
    si, ei = min(ai, bi), max(ai, bi) + 1
    sj, ej = min(aj, bj), max(aj, bj) + 1
    if ai == bi:
        return {(ai, j) for j in range(sj, ej)}
    if aj == bj:
        return {(i, aj) for i in range(si, ei)}
    if bi - ai == bj - aj:
        return {(i, j) for i, j in zip(range(si, ei), range(sj, ej))}
    if bi - ai == aj - bj:
        return {(i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1))}
    return set()

def _shoot(start, direction):
    return _connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

def _fill(grid, value, indices):
    h, w = len(grid), len(grid[0])
    out = [list(r) for r in grid]
    for i, j in _to_indices(indices):
        if 0 <= i < h and 0 <= j < w:
        out[i][j] = value
    return out

def _underfill(grid, value, indices):
    h, w = len(grid), len(grid[0])
    bg = _mostcolor(grid)
    out = [list(r) for r in grid]
    for i, j in _to_indices(indices):
        if 0 <= i < h and 0 <= j < w and out[i][j] == bg:
        out[i][j] = value
    return out

def solve_b527c5c6(I):
    objs = _objects(I)
    shot_lines = []
    for obj in objs:
        two_idx = {idx for (v, idx) in obj if v == TWO}
        if not two_idx:
        continue
        at_bottom = _lowermost(two_idx) == _lowermost(obj)
        at_right  = _rightmost(two_idx) == _rightmost(obj)
        at_top    = _uppermost(two_idx) == _uppermost(obj)
        at_left   = _leftmost(two_idx) == _leftmost(obj)
        di = (1 if at_bottom else 0) + (-1 if at_top else 0)
        dj = (1 if at_right else 0) + (-1 if at_left else 0)
        ci = _uppermost(two_idx) + _height(two_idx) // 2
        cj = _leftmost(two_idx) + _width(two_idx) // 2
        line = _shoot((ci, cj), (di, dj))
        shot_lines.append(line)
    all_lines = {p for line in shot_lines for p in line}
    grid = _fill(I, TWO, all_lines)
    thick = set()
    for obj, line in zip(objs, shot_lines):
        is_vert = _vline(line)
        k = min(_height(obj), _width(obj))
        for off in range(-(k - 1), k):
        if is_vert:
        thick.update({(i, j + off) for (i, j) in line})
        else:
        thick.update({(i + off, j) for (i, j) in line})
    return _underfill(grid, THREE, thick)

def p(g):
    return solve_b527c5c6(g)
