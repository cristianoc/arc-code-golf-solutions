# ARC Task 202

def p(g):
    # If no uniform row exists, transpose to make one exist
    def transpose(a):
        return [list(r) for r in zip(*a)]

    def has_uniform_row(a):
        return any(len(set(row)) == 1 for row in a)

    G = [r[:] for r in g]
    transposed = False
    if not has_uniform_row(G):
        G = transpose(G)
        transposed = True

    h, w = len(G), len(G[0])
    # Build color partitions' bounding boxes (for colors != 0)
    positions = {}
    for i in range(h):
        for j in range(w):
        v = G[i][j]
        if v == 0:
        continue
        positions.setdefault(v, []).append((i, j))

    # Determine zero columns per color bounding box based on the original G
    zero_cols_by_color = {}
    bbox_by_color = {}
    for v, pts in positions.items():
        i0 = min(i for i, _ in pts)
        i1 = max(i for i, _ in pts)
        j0 = min(j for _, j in pts)
        j1 = max(j for _, j in pts)
        bbox_by_color[v] = (i0, i1, j0, j1)
        zc = set()
        for j in range(j0, j1 + 1):
        found_zero = False
        for i in range(i0, i1 + 1):
        if G[i][j] == 0:
        found_zero = True
        break
        if found_zero:
        zc.add(j)
        zero_cols_by_color[v] = zc

    # Apply zeroing only within the color piece
    O = [r[:] for r in G]
    for v, pts in positions.items():
        zc = zero_cols_by_color[v]
        if not zc:
        continue
        for (i, j) in pts:
        if j in zc:
        O[i][j] = 0

    if transposed:
        O = transpose(O)
    return O
