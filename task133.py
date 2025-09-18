# ARC Task 133

def p(g):
    H, W = len(g), len(g[0])
    flat = [v for r in g for v in r]
    bg = max(set(flat), key = flat.count)

    def inb(i, j):
        return 0 <= i < H and 0 <= j < W

    # 8 - connected components of non - background (colors may mix)
    def comps8():
        seen = [[False] * W for _ in range(H)]
        out = []
        for i in range(H):
        for j in range(W):
        if seen[i][j] or g[i][j] == bg:
        continue
        q, comp = [(i, j)], set()
        seen[i][j] = True
        while q:
        ci, cj = q.pop()
        comp.add((ci, cj))
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        ni, nj = ci + di, cj + dj
        if inb(ni, nj) and not seen[ni][nj] and g[ni][nj] != bg:
        seen[ni][nj] = True
        q.append((ni, nj))
        out.append(comp)
        return out

    # 4 - connected, univalued non - bg components -> list of (color, cells)
    def comps4():
        seen = [[False] * W for _ in range(H)]
        out = []
        for i in range(H):
        for j in range(W):
        if seen[i][j] or g[i][j] == bg:
        continue
        c = g[i][j]
        q, cells = [(i, j)], set()
        seen[i][j] = True
        while q:
        ci, cj = q.pop()
        cells.add((ci, cj))
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if inb(ni, nj) and not seen[ni][nj] and g[ni][nj] == c:
        seen[ni][nj] = True
        q.append((ni, nj))
        out.append((c, cells))
        return out

    # Pick 8 - connected component maximizing (max color count - min color count)
    c8 = comps8()
    if not c8:
        return [row[:] for row in g]

    def sc(cells):
        cnt = {}
        for i, j in cells:
        v = g[i][j]
        cnt[v] = cnt.get(v, 0) + 1
        return (max(cnt.values()) - min(cnt.values())) if cnt else -10**9

    major = max(c8, key = sc)

    # Least - frequent color inside major (tie: min color value)
    vals = [g[i][j] for i, j in major]
    least = min(set(vals), key = vals.count)

    # Normalize major to (0, 0) and find ulcorner of least - colored subset
    mi0, mj0 = min(i for i, _ in major), min(j for _, j in major)
    major_n = {(i - mi0, j - mj0) for i, j in major}
    lsub = {(i - mi0, j - mj0) for i, j in major if g[i][j] == least}
    if lsub:
        li, lj = min(i for i, _ in lsub), min(j for _, j in lsub)
    else:
        li = lj = 0

    # Helpers on cell sets
    def bbox(S):
        is_ = [i for i, _ in S]
        js_ = [j for _, j in S]
        return min(is_), min(js_), max(is_), max(js_)

    def width(S):
        u, l, d, r = bbox(S)
        return r - l + 1

    def ulcorner(S):
        u, l, _, _ = bbox(S)
        return u, l

    def outbox_ring(S):
        u, l, d, r = bbox(S)
        si, sj, ei, ej = u - 1, l - 1, d + 1, r + 1
        V = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
        Hh = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
        return V | Hh

    comps = comps4()
    least_comps = [cells for c, cells in comps if c == least]

    patches = []  # (color, indices)
    for cells in least_comps:
        w = width(cells)
        ui, uj = ulcorner(cells)
        # color from outbox ring (prefer non - zero)
        ring = outbox_ring(cells)
        pal = {g[i][j] for i, j in ring if inb(i, j)}
        pal.discard(0)
        recol = next(iter(pal)) if pal else 0

        # shift normalized major by (ui - li * w, uj - lj * w)
        si, sj = ui - li * w, uj - lj * w
        shifted = {(i + si, j + sj) for i, j in major_n}
        if shifted:
        u2 = min(i for i, _ in shifted)
        l2 = min(j for _, j in shifted)
        else:
        u2 = l2 = 0
        idx = set()
        for ti, tj in shifted:
        ni, nj = ti - u2, tj - l2
        bi, bj = u2 + ni * w, l2 + nj * w
        for a in range(w):
        for b in range(w):
        ii, jj = bi + a, bj + b
        if inb(ii, jj):
        idx.add((ii, jj))
        patches.append((recol, idx))

    G = [row[:] for row in g]
    for c, idx in patches:
        for i, j in idx:
        G[i][j] = c
    # restore original univalued non - bg components
    for c, cells in comps:
        for i, j in cells:
        G[i][j] = c
    return G
