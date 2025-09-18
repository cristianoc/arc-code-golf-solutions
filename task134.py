# ARC Task 134

def p(g):
    # Non - DSL solution for 5ad4f10b (task134)
    # Robust rule distilled from examples:
    # - Treat background as 0 when present (not "most frequent").
    # - Among non - background, pick the "object" color as the chunkier one
    #   (higher average 4 - neighbor adjacency; break ties by global count).
    # - The other non - background color is the accent used in the 3x3 output
    #   (least frequent among non - background colors).
    # - Compute the bounding box of ALL pixels of the object color (no comp split).
    # - Downsample that bbox into a 3x3 grid: mark a cell with the accent color
    #   iff any object pixel falls inside the corresponding sub - rectangle; else 0.
    from collections import Counter

    grid = [row[:] for row in g]
    H, W = len(grid), len(grid[0])

    counts = Counter(v for r in grid for v in r)
    bg = 0 if 0 in counts else max(counts, key = counts.get)

    # Candidate colors exclude the background
    colors = [c for c in counts if c != bg]
    # If we have fewer than 2 colors, just return a zero 3x3
    if len([c for c in colors if c != 0]) == 0:
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Chunkiness via average number of 4 - neighbors of the same color per pixel
    def avg_neighbors(col: int) -> float:
        s = 0
        n = 0
        for i in range(H):
        row = grid[i]
        for j in range(W):
        if row[j] != col:
        continue
        n += 1
        if i > 0 and grid[i - 1][j] == col:
        s += 1
        if i + 1 < H and grid[i + 1][j] == col:
        s += 1
        if j > 0 and row[j - 1] == col:
        s += 1
        if j + 1 < W and row[j + 1] == col:
        s += 1
        return s / (n or 1)

    nonzero_colors = [c for c in colors if c != 0]
    # Object: chunkier first, then by global count
    obj = max(nonzero_colors, key = lambda c: (avg_neighbors(c), counts[c], -c))
    # Accent: remaining nonzero color with least global count (ties -> smaller id)
    rem = [c for c in nonzero_colors if c != obj]
    accent = min(rem, key = lambda c: (counts[c], c)) if rem else obj

    # Bounding box of ALL pixels of the object color (ignore components)
    coords = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == obj]
    if not coords:
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    mi = min(i for i, _ in coords)
    mj = min(j for _, j in coords)
    Ma = max(i for i, _ in coords)
    Mb = max(j for _, j in coords)


    ri = (mi, mi + (Ma - mi + 1) // 3, mi + (2 * (Ma - mi + 1)) // 3, Ma + 1)
    cj = (mj, mj + (Mb - mj + 1) // 3, mj + (2 * (Mb - mj + 1)) // 3, Mb + 1)

    out = []
    for r in range(3):
        row = []
        for c in range(3):
        any_obj = False
        for i in range(ri[r], ri[r + 1]):
        for j in range(cj[c], cj[c + 1]):
        if 0 <= i < H and 0 <= j < W and grid[i][j] == obj:
        any_obj = True
        break
        if any_obj:
        break
        row.append(accent if any_obj else 0)
        out.append(row)
    return out
