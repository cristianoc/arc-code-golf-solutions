def solve_22233c11(I):
    # Compact, non-DSL reimplementation preserving original behavior.
    H, W = len(I), len(I[0])

    # Background color (most frequent)
    vals = [v for r in I for v in r]
    bg = max(set(vals), key=vals.count)

    # 8-connected components excluding background
    def neighbors8(i, j):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W:
                    yield ni, nj

    seen = [[False] * W for _ in range(H)]
    objects = []  # list of (color, indices)
    for i in range(H):
        for j in range(W):
            if seen[i][j] or I[i][j] == bg:
                continue
            c = I[i][j]
            stack = [(i, j)]
            seen[i][j] = True
            idx = []
            while stack:
                ci, cj = stack.pop()
                if I[ci][cj] != c:
                    continue
                idx.append((ci, cj))
                for ni, nj in neighbors8(ci, cj):
                    if not seen[ni][nj] and I[ni][nj] != bg and I[ni][nj] == c:
                        seen[ni][nj] = True
                        stack.append((ni, nj))
            if idx:
                objects.append((c, idx))

    # Helpers on index sets
    def ul_lr(indices):
        mi = min(i for i, _ in indices); mj = min(j for _, j in indices)
        Mi = max(i for i, _ in indices); Mj = max(j for _, j in indices)
        return (mi, mj), (Mi, Mj)

    def vmirror_indices(indices):
        (mi, mj), (Mi, Mj) = ul_lr(indices)
        d = mj + Mj
        return [(i, d - j) for i, j in indices]

    def upscale_indices(indices, factor):
        if not indices:
            return []
        (mi, mj), _ = ul_lr(indices)
        norm = [(i - mi, j - mj) for i, j in indices]
        out = []
        for i, j in norm:
            for io in range(factor):
                for jo in range(factor):
                    out.append((i * factor + io, j * factor + jo))
        # shift back
        return [(i + mi, j + mj) for i, j in out]

    def shape(indices):
        (mi, mj), (Mi, Mj) = ul_lr(indices)
        return (Mi - mi + 1, Mj - mj + 1)

    # Build fill mask
    mark = set()
    for _, idx in objects:
        if not idx:
            continue
        # S = vmirror(idx) then upscale by 2, then shift by - (h//2, w//2)
        S = vmirror_indices(idx)
        S = upscale_indices(S, 2)
        h, w = shape(idx)  # use original shape per original code
        off_i, off_j = -(h // 2), -(w // 2)
        S = [(i + off_i, j + off_j) for i, j in S]

        # Crosshair lines for original idx over a 30x30 canvas
        J = set()
        for i, j in idx:
            for jj in range(30):
                J.add((i, jj))
            for ii in range(30):
                J.add((ii, j))

        # D = S - J; add those inside bounds
        for i, j in S:
            if (i, j) not in J and 0 <= i < H and 0 <= j < W:
                mark.add((i, j))

    # Fill with color 8 at marked positions
    out = [row[:] for row in I]
    for i, j in mark:
        out[i][j] = 8
    return out

def p(g):
    try:
        return solve_22233c11([row[:] for row in g])
    except Exception:
        return [list(r) for r in g]

