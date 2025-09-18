# ARC Task 034

def solve_1f0c79e5(I):
    # Compact, non - DSL reimplementation preserving original behavior.
    H, W = len(I), len(I[0])

    # coords where color == 2
    coords2 = [(i, j) for i in range(H) for j in range(W) if I[i][j] == 2]

    # Grid with 2 -> 0, then find least frequent color
    g2 = [row[:] for row in I]
    for i, j in coords2:
        g2[i][j] = 0
    vals = [v for r in g2 for v in r]
    colors = set(vals)
    least = min(colors, key = vals.count)

    # Coordinates of that least frequent color on g2
    coords_least = [(i, j) for i in range(H) for j in range(W) if g2[i][j] == least]

    # Union shape S; if empty, return input
    S = coords2 + coords_least
    if not S:
        return [row[:] for row in I]

    # UL corner of S and normalized coords of 2's relative to it
    min_i = min(i for i, _ in S)
    min_j = min(j for _, j in S)
    norm2 = [(i - min_i, j - min_j) for i, j in coords2]

    # Build offsets k*(2 * i - 1, 2 * j - 1) for k in 0..8 and (i, j) in norm2
    offsets = []
    for i, j in norm2:
        di, dj = 2 * i - 1, 2 * j - 1
        for k in range(9):
        offsets.append((di * k, dj * k))

    # Paint S shifted by each offset with color `least`
    out = [row[:] for row in I]
    for off_i, off_j in offsets:
        for i, j in S:
        ni, nj = i + off_i, j + off_j
        if 0 <= ni < H and 0 <= nj < W:
        out[ni][nj] = least
    return out

def p(g):
    try:
        return solve_1f0c79e5([row[:] for row in g])
    except Exception:
        return [list(r) for r in g]
