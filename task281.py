from collections import Counter

def p(g):
    h, w = len(g), len(g[0])

    # Background = most frequent color
    vals = [v for r in g for v in r]
    bg = Counter(vals).most_common(1)[0][0]

    # All non-background indices; if none, return copy
    idx = [(i, j) for i in range(h) for j in range(w) if g[i][j] != bg]
    if not idx:
        return [row[:] for row in g]

    # Least frequent color after mapping 8->0, then next least after removing the first
    def least_color(grid):
        vs = [v for r in grid for v in r]
        return min(set(vs), key=vs.count)

    def replace_color(grid, a, b):
        return tuple(tuple(b if v == a else v for v in r) for r in grid)

    grid_no8 = replace_color(g, 8, 0)
    c1 = least_color(grid_no8)
    c2 = least_color(replace_color(grid_no8, c1, 0))

    ui = min(i for i, _ in idx)
    li = max(i for i, _ in idx)
    uj = min(j for _, j in idx)
    lj = max(j for _, j in idx)

    out = [row[:] for row in g]
    for i in range(ui, li + 1):
        for j in range(uj, lj + 1):
            out[i][j] = c1
    for j in range(uj, lj + 1):
        out[ui][j] = c2
        out[li][j] = c2
    for i in range(ui, li + 1):
        out[i][uj] = c2
        out[i][lj] = c2
    return out

