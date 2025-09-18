# ARC Task 341

def p(g):
    # Compact, non - DSL implementation of d6ad076f
    I = tuple(tuple(r) for r in g)
    h, w = len(I), len(I[0])

    def most_color(G):
        from collections import Counter
        c = Counter(v for row in G for v in row)
        return max(c.items(), key = lambda kv: kv[1])[0]

    bg = most_color(I)

    # 4 - connected components by color (excluding background)
    seen = [[False] * w for _ in range(h)]
    comps = []  # list of (color, cells)

    def n4(i, j):
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w:
        yield ni, nj

    for i in range(h):
        for j in range(w):
        if seen[i][j]:
        continue
        seen[i][j] = True
        v = I[i][j]
        if v == bg:
        continue
        stack = [(i, j)]
        cells = []
        while stack:
        ci, cj = stack.pop()
        cells.append((ci, cj))
        for ni, nj in n4(ci, cj):
        if not seen[ni][nj] and I[ni][nj] == v:
        seen[ni][nj] = True
        stack.append((ni, nj))
        comps.append((v, cells))

    if len(comps) < 2:
        return [list(row) for row in I]

    # Prefer first two as in original; otherwise min/max size fallback
    x2, x3 = comps[0], comps[1]
    # centers and spans
    def bbox(cells):
        is_ = [i for i, j in cells]
        js_ = [j for i, j in cells]
        return min(is_), min(js_), max(is_), max(js_)

    def center(cells):
        mi, mj, Mi, Mj = bbox(cells)
        return (mi + (Mi - mi) // 2, mj + (Mj - mj) // 2)

    def inbox_ring(cells):
        mi, mj, Mi, Mj = bbox(cells)
        ai, aj = mi + 1, mj + 1
        bi, bj = Mi - 1, Mj - 1
        si, sj = min(ai, bi), min(aj, bj)
        ei, ej = max(ai, bi), max(aj, bj)
        if ei < si or ej < sj:
        return set()
        vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
        hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
        return vlines | hlines

    # Determine mode (vertical vs horizontal) by shared columns with larger object
    cols2 = {j for _, j in x2[1]}
    cols3 = {j for _, j in x3[1]}
    rows2 = {i for i, _ in x2[1]}
    rows3 = {i for i, _ in x3[1]}
    vertical = len(cols2 & cols3) > 0

    # Direction from smaller to larger along chosen axis
    ci2, cj2 = center(x2[1])
    ci3, cj3 = center(x3[1])
    if vertical:
        step = (1 if ci2 < ci3 else -1, 0)
    else:
        step = (0, 1 if cj2 < cj3 else -1)

    # Starting ring on inner perimeter of the smaller object
    starts = inbox_ring(x2[1])
    # Restrict starts to interior span of the larger object along orthogonal axis
    if vertical:
        lj, rj = min(cols3) + 1, max(cols3) - 1
        starts = {(i, j) for (i, j) in starts if lj <= j <= rj}
    else:
        ui, li = min(rows3) + 1, max(rows3) - 1
        starts = {(i, j) for (i, j) in starts if ui <= i <= li}

    # Underfill rays with color 8 (only paint background)
    out = [list(row) for row in I]
    for si, sj in starts:
        i, j = si, sj
        while 0 <= i < h and 0 <= j < w:
        if out[i][j] == bg:
        out[i][j] = 8
        i += step[0]
        j += step[1]

    # Remove cyan components that touch the border
    seen2 = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
        if seen2[i][j]:
        continue
        seen2[i][j] = True
        if out[i][j] != 8:
        continue
        stack = [(i, j)]
        cells = []
        border = False
        while stack:
        ci, cj = stack.pop()
        cells.append((ci, cj))
        if ci == 0 or ci == h - 1 or cj == 0 or cj == w - 1:
        border = True
        for ni, nj in n4(ci, cj):
        if not seen2[ni][nj] and out[ni][nj] == 8:
        seen2[ni][nj] = True
        stack.append((ni, nj))
        if border:
        for ci, cj in cells:
        out[ci][cj] = bg

    return out
