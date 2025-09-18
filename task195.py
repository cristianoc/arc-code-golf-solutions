# ARC Task 195

def p(g):
    # Find most frequent color (background)
    h, w = len(g), len(g[0])
    flat = [v for r in g for v in r]
    bg = max(set(flat), key = flat.count)
    # Bounding box of non - background
    coords = [(i, j) for i in range(h) for j in range(w) if g[i][j] != bg]
    if not coords:
        return [list(r) for r in g]
    i0 = min(i for i, _ in coords)
    i1 = max(i for i, _ in coords)
    j0 = min(j for _, j in coords)
    j1 = max(j for _, j in coords)
    H, W = i1 - i0 + 1, j1 - j0 + 1
    # Equivalent to: upscale vs tiled compare then downscale by 3
    out = [[0 for _ in range(W)] for __ in range(H)]
    for a in range(H):
        for b in range(W):
        v1 = g[i0 + a][j0 + b]
        v2 = g[i0 + (3 * a) % H][j0 + (3 * b) % W]
        out[a][b] = v1 if v1 == v2 else 0
    return out
