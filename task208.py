def p(g):
    # Draw a ring of the least frequent color around a zero-filled hole
    # whose inner size matches the color's bbox minus the border.
    H, W = len(g), len(g[0])
    from collections import Counter

    # Least frequent color in the whole grid
    cnt = Counter(v for r in g for v in r)
    c = min(cnt, key=cnt.get)

    # Bounding box of color c
    coords = [(i, j) for i in range(H) for j in range(W) if g[i][j] == c]
    if not coords:
        return [row[:] for row in g]
    top = min(i for i, _ in coords)
    left = min(j for _, j in coords)
    bot = max(i for i, _ in coords)
    right = max(j for _, j in coords)
    h = bot - top + 1
    w = right - left + 1
    ih = max(1, h - 2)
    iw = max(1, w - 2)

    def is_existing_ring(i, j):
        # True if the border at (i,j,h,w) is already all color c
        for b in range(j, j + w):
            if g[i][b] != c or g[i + h - 1][b] != c:
                return False
        for a in range(i, i + h):
            if g[a][j] != c or g[a][j + w - 1] != c:
                return False
        return True

    # Find the first location with an inner zero-filled rectangle (ih x iw)
    target = None
    for i in range(H - (ih + 2) + 1):
        for j in range(W - (iw + 2) + 1):
            ok = True
            for a in range(i + 1, i + ih + 1):
                row = g[a]
                for b in range(j + 1, j + iw + 1):
                    if row[b] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                # Prefer a hole that is not already surrounded by color c
                if target is None or is_existing_ring(*target) and not is_existing_ring(i, j):
                    target = (i, j)
        
    if target is None:
        return [row[:] for row in g]

    i, j = target
    h = ih + 2
    w = iw + 2
    out = [row[:] for row in g]
    for b in range(j, j + w):
        out[i][b] = c
        out[i + h - 1][b] = c
    for a in range(i, i + h):
        out[a][j] = c
        out[a][j + w - 1] = c
    return out

