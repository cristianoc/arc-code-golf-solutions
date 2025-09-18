# ARC Task 173

"""Refactored solution for task 173 (72322fa7) without frozenset.

Behavior preserved:
- Find 8 - connected non - background objects (background = most common color).
- For each multi - color object, split into majority - colored pixels (major)
    and the remaining pixels (minor).
- Stamp the full object wherever the major subpattern occurs.
- Also stamp the full object wherever the minor subpattern occurs, offset so
    that the full object's UL corner aligns relative to the minor's UL corner.
- Apply paints from major matches first, then from minor matches.
Output is a list - of - lists grid.
"""

from collections import deque, Counter


def most_common_in_grid(G):
    flat = [v for row in G for v in row]
    return Counter(flat).most_common(1)[0][0]


def find_objects(G):
    """Return list of objects
    each object is a list of (v, i, j).
    Objects are 8 - connected components of non - background cells.
    """
    H, W = len(G), len(G[0])
    bg = most_common_in_grid(G)
    seen = [[False] * W for _ in range(H)]
    objs = []

    for si in range(H):
        for sj in range(W):
        if seen[si][sj] or G[si][sj] == bg:
        continue
        comp = []
        dq = deque([(si, sj)])
        seen[si][sj] = True
        while dq:
        i, j = dq.popleft()
        comp.append((G[i][j], i, j))
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and not seen[ni][nj] and G[ni][nj] != bg:
        seen[ni][nj] = True
        dq.append((ni, nj))
        objs.append(comp)
    return objs


def num_colors(obj):
    return len({v for v, _, _ in obj})


def most_common_in_obj(obj):
    cnt = Counter(v for v, _, _ in obj)
    return cnt.most_common(1)[0][0]


def ulcorner_obj(obj):
    is_ = [i for _, i, _ in obj]
    js_ = [j for _, _, j in obj]
    return (min(is_), min(js_))


def normalize_obj(obj):
    if not obj:
        return obj
    ui, uj = ulcorner_obj(obj)
    return [(v, i - ui, j - uj) for (v, i, j) in obj]


def obj_shape_from_points(points):
    if not points:
        return (0, 0)
    is_ = [i for _, i, _ in points]
    js_ = [j for _, _, j in points]
    return (max(is_) - min(is_) + 1, max(js_) - min(js_) + 1)


def occurrences(G, sub_points):
    """All (i, j) where normalized subpattern matches G.
    sub_points: list of (v, i, j) absolute coords
    normalization is internal.
    """
    H, W = len(G), len(G[0])
    sub_norm = normalize_obj(sub_points)
    h, w = obj_shape_from_points(sub_points)
    occ = []
    for i in range(H - h + 1):
        for j in range(W - w + 1):
        ok = True
        for v, a, b in sub_norm:
        if G[i + a][j + b] != v:
        ok = False
        break
        if ok:
        occ.append((i, j))
    return occ


def stamp(grid, origin_i, origin_j, rel_points):
    H, W = len(grid), len(grid[0])
    for v, a, b in rel_points:
        i, j = origin_i + a, origin_j + b
        if 0 <= i < H and 0 <= j < W:
        grid[i][j] = v


def solve_72322fa7(I):
    # Work with a list - of - lists grid throughout.
    G = [row[:] for row in I]

    objs = find_objects(G)

    # First pass: apply major matches; second: minor matches.
    major_stamps = []  # each: (origin_i, origin_j, rel_points)
    minor_stamps = []

    for obj in objs:
        if num_colors(obj) == 1:
        continue

        mc = most_common_in_obj(obj)
        major = [(v, i, j) for (v, i, j) in obj if v == mc]
        minor = [(v, i, j) for (v, i, j) in obj if v != mc]

        if not major or not minor:
        continue

        occ_major = occurrences(G, major)
        occ_minor = occurrences(G, minor)

        uo_i, uo_j = ulcorner_obj(obj)
        um_i, um_j = ulcorner_obj(minor)
        delta_i, delta_j = (uo_i - um_i, uo_j - um_j)

        norm_obj = normalize_obj(obj)

        for oi, oj in occ_major:
        major_stamps.append((oi, oj, norm_obj))

        for pi, pj in occ_minor:
        oi, oj = pi + delta_i, pj + delta_j
        minor_stamps.append((oi, oj, norm_obj))

    out = [row[:] for row in G]
    for oi, oj, rel in major_stamps:
        stamp(out, oi, oj, rel)
    for oi, oj, rel in minor_stamps:
        stamp(out, oi, oj, rel)
    return out


def p(g):
    return solve_72322fa7(g)
