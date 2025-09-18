# ARC Task 054

def p(g):
    # Compact non - DSL reimplementation of task 054
    h, w = len(g), len(g[0])

    # Background color (most frequent)
    flat = [v for r in g for v in r]
    cnt = {}
    for v in flat:
        cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key = cnt.get)

    # Helper to collect 4 - connected components over non - background cells
    def components(grid):
        seen = [[False] * w for _ in range(h)]
        res = []
        for i in range(h):
        for j in range(w):
        if grid[i][j] == bg or seen[i][j]:
        continue
        q = [(i, j)]
        seen[i][j] = True
        cells = []
        mi, mj, Ma, Mj = i, j, i, j
        while q:
        a, b = q.pop()
        cells.append((a, b, grid[a][b]))
        if a < mi: mi = a
        if b < mj: mj = b
        if a > Ma: Ma = a
        if b > Mj: Mj = b
        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        na, nb = a + da, b + db
        if 0 <= na < h and 0 <= nb < w and not seen[na][nb] and grid[na][nb] != bg:
        seen[na][nb] = True
        q.append((na, nb))
        res.append((cells, (mi, mj, Ma, Mj)))
        return res

    comps_orig = components(g)
    if not comps_orig:
        return [row[:] for row in g]

    # Smallest component by size in original grid
    cells, (mi, mj, Ma, Mj) = min(comps_orig, key = lambda x: len(x[0]))
    H, W = (Ma - mi + 1), (Mj - mj + 1)

    # Center of its bounding box and its colors in original grid
    ci, cj = mi + (Ma - mi) // 2, mj + (Mj - mj) // 2
    c0 = g[ci][cj]
    # Neighbor direction: UP if height==5 else RIGHT
    ni, nj = (-1, 0) if H == 5 else (0, 1)
    neigh = g[ci + ni][cj + nj] if 0 <= ci + ni < h and 0 <= cj + nj < w else None

    # Remove the smallest component from the grid (paint to bg)
    out = [row[:] for row in g]
    for a, b, _ in cells:
        out[a][b] = bg

    # Occurrences of color c0 in the modified grid BEFORE line drawing (matches DSL)
    occ = []
    for i in range(h):
        for j in range(w):
        if out[i][j] == c0:
        occ.append((i, j))

    # Build components on the modified grid and draw lines over each object's bounding box
    comps_mod = components(out)
    # Keep a copy of background - mask (positions that are bg in x18)
    bg_mask = [[out[i][j] == bg for j in range(w)] for i in range(h)]
    draw_vertical = (H == 5) or (W != 5)
    draw_horizontal = (W == 5) or (H != 5)
    if neigh is not None:
        for ccells, (r0, c0_, r1, c1) in comps_mod:
        # Subgrid bounds
        rh, rw = r1 - r0 + 1, c1 - c0_ + 1
        # Find occurrences of color c0 inside this rectangle (in the modified grid)
        for i in range(rh):
        for j in range(rw):
        if out[r0 + i][c0_ + j] == c0:
        if draw_vertical:
        for ii in range(rh):
        out[r0 + ii][c0_ + j] = neigh
        if draw_horizontal:
        for jj in range(rw):
        out[r0 + i][c0_ + jj] = neigh

    # Normalized smallest component cells and shift based on size rules
    norm = [(a - mi, b - mj, col) for (a, b, col) in cells]
    si = -1 - (1 if H == 5 else 0)
    sj = -1 - (1 if W == 5 else 0)
    for i, j in occ:
        for di, dj, col in norm:
        ai, aj = i + si + di, j + sj + dj
        if 0 <= ai < h and 0 <= aj < w:
        out[ai][aj] = col

    # Final mask: restore background at positions that were bg in x18
    for i in range(h):
        for j in range(w):
        if bg_mask[i][j]:
        out[i][j] = bg

    return out
