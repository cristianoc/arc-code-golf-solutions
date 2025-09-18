# ARC Task 219

def p(g):
    # Simplified, non - DSL solution for 90f3ed37 (task219)
    if not g or not g[0]:  # guard empty grids
        return [row[:] for row in g]

    G = [row[:] for row in g]
    H, W = len(G), len(G[0])

    from collections import Counter

    def most_color(grid):
        c = Counter(v for r in grid for v in r)
        return max(c, key = lambda k: c[k])

    def diag_neighbors(i, j):
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        ii, jj = i + di, j + dj
        if 0 <= ii < H and 0 <= jj < W:
        yield (ii, jj)

    def objects_univalued_8c_nonbg(grid):
        bg = most_color(grid)
        h, w = len(grid), len(grid[0])
        occupied = set()
        objs = []
        for i in range(h):
        for j in range(w):
        if (i, j) in occupied:
        continue
        v0 = grid[i][j]
        if v0 == bg:
        continue
        pts = set()
        frontier = {(i, j)}
        while frontier:
        neighborhood = set()
        for a, b in frontier:
        if (a, b) in occupied:
        continue
        v = grid[a][b]
        if v == v0:
        pts.add((a, b))
        occupied.add((a, b))
        for na, nb in diag_neighbors(a, b):
        if 0 <= na < h and 0 <= nb < w:
        neighborhood.add((na, nb))
        frontier = neighborhood - occupied
        if pts:
        objs.append((v0, tuple(sorted(pts))))
        return objs

    def uppermost(points):
        return min(i for i, _ in points)

    def ulcorner(points):
        return (min(i for i, _ in points), min(j for _, j in points))

    def normalize(col_points):
        col, pts = col_points
        ui, uj = ulcorner(pts)
        return (col, tuple(sorted((i - ui, j - uj) for i, j in pts)))

    def shift(col_points, dv):
        col, pts = col_points
        di, dj = dv
        return (col, tuple(sorted((i + di, j + dj) for i, j in pts)))

    bg = most_color(G)
    # Detect objects and deduplicate by point - set (avoid accidental duplicates)
    raw_objs = objects_univalued_8c_nonbg(G)
    uniq = {}
    for col, pts in raw_objs:
        uniq[pts] = col
    objs = [(col, pts) for pts, col in uniq.items()]
    if not objs:
        return [row[:] for row in G]

    # Top - most band can consist of multiple disjoint blobs (e.g. staggered 8s).
    # Merge every object that lies within that contiguous band so the template
    # captures the full pattern we want to project onto lower copies.
    objs_sorted = sorted(objs, key = lambda cp: (uppermost(cp[1]), ulcorner(cp[1])[1]))
    top_row = uppermost(objs_sorted[0][1])
    band_bottom = top_row
    for r in range(top_row + 1, H):
        if any(G[r][c] != bg for c in range(W)):
        band_bottom = r
        elif band_bottom >= top_row:
        break

    template_pts = set()
    template_color = objs_sorted[0][0]
    for col, pts in objs_sorted:
        if uppermost(pts) <= band_bottom:
        template_pts.update(pts)
        else:
        break
    ui = min(i for i, _ in template_pts)
    uj = min(j for _, j in template_pts)
    base_pts = tuple(sorted((i - ui, j - uj) for i, j in template_pts))
    base_norm = (template_color, base_pts)

    def merge_objects(seq):
        groups = []
        current = None
        max_row = -1
        for col, pts in seq:
        top = uppermost(pts)
        if top <= band_bottom:
        continue
        low = max(i for i, _ in pts)
        if current is None or top > max_row + 1:
        if current is not None:
        groups.append((template_color, tuple(sorted(current))))
        current = set(pts)
        max_row = low
        else:
        current.update(pts)
        if low > max_row:
        max_row = low
        if current is not None:
        groups.append((template_color, tuple(sorted(current))))
        return groups

    others = merge_objects(objs_sorted)

    # Try multiple shift patterns - be more flexible
    shifts = [(0, 2), (0, 1), (0, 0), (0, -1), (0, -2), (-1, 0)]
    chosen = []
    for col, pts in others:
        anchor = ulcorner(pts)
        placed = shift(base_norm, anchor)
        cand_sets = [set(shift(placed, dv)[1]) for dv in shifts]
        # Score by intersection size with the target object (position match only)
        target_vals = set(pts)
        scored_sets = [(s, len(s & target_vals), min(i for i, _ in s) if s else float('inf')) for s in cand_sets]
        # Use the best match, fallback to original if no good match
        best_score = max(scored_sets, key = lambda x: (x[1], -x[2]))
        max_col = max(j for _, j in pts)
        if best_score[1] > 0:
        chosen.append((best_score[0], max_col))
        else:
        # Fallback to original object position if no good template match
        chosen.append((target_vals, max_col))

    # Underfill 1's beneath background cells within union of chosen patches
    O = [row[:] for row in G]
    for s, limit in chosen:
        for (i, j) in s:
        if j <= limit:
        continue
        if 0 <= i < H and 0 <= j < W and O[i][j] == bg:
        O[i][j] = 1
    return O
