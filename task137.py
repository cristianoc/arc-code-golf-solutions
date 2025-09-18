# ARC Task 137

def p(g):
    # Compact non - DSL solution for 5c2c9af4 (task137)
    G = [row[:] for row in g]
    H, W = len(G), len(G[0])
    from collections import Counter
    # Least frequent color in the grid
    cnt = Counter(v for r in G for v in r)
    least = min(cnt, key = lambda c: cnt[c])
    # Indices of that color
    pts = [(i, j) for i in range(H) for j in range(W) if G[i][j] == least]
    if not pts:
        return [row[:] for row in g]
    min_i = min(i for i, _ in pts)
    max_i = max(i for i, _ in pts)
    min_j = min(j for _, j in pts)
    max_j = max(j for _, j in pts)
    ci = min_i + (max_i - min_i) // 2
    cj = min_j + (max_j - min_j) // 2
    vi = ci - min_i
    vj = cj - min_j

    def add_box(mask, a, b):
        ai, aj = a
        bi, bj = b
        si, ei = (ai, bi) if ai <= bi else (bi, ai)
        sj, ej = (aj, bj) if aj <= bj else (bj, aj)
        for i in range(si, ei + 1):
        mask.add((i, sj))
        mask.add((i, ej))
        for j in range(sj, ej + 1):
        mask.add((si, j))
        mask.add((ei, j))

    mask = set()
    # Expand boxes sufficiently to reach grid boundaries
    K = max(H, W)
    for k in range(0, K):
        a = (k * vi, k * vj)
        b = (-k * vi, -k * vj)
        local = set()
        add_box(local, a, b)
        for i, j in local:
        ii, jj = ci + i, cj + j
        if 0 <= ii < H and 0 <= jj < W:
        mask.add((ii, jj))

    O = [row[:] for row in G]
    for i, j in mask:
        O[i][j] = least
    return O
