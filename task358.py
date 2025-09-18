# ARC Task 358

def solve_e21d9049(I):
    G = [row[:] for row in I]
    H, W = len(G), len(G[0])

    # Background color
    from collections import Counter
    bg = Counter([v for r in G for v in r]).most_common(1)[0][0]

    # Collect all non - bg cells (union of objects)
    cells = [(i, j) for i in range(H) for j in range(W) if G[i][j] != bg]
    if not cells:
        return G

    # Pivot row and column = most populated among motif cells
    rc = Counter(i for i, _ in cells)
    cc = Counter(j for _, j in cells)
    pr = max(rc, key = rc.get)
    pc = max(cc, key = cc.get)

    # Extract ordered color sequences along pivot row/column, using motif cells only
    row_cells = sorted((j, G[pr][j]) for j in range(W) if (pr, j) in set(cells))
    col_cells = sorted((i, G[i][pc]) for i in range(H) if (i, pc) in set(cells))
    row_seq = [c for _, c in row_cells]
    col_seq = [c for _, c in col_cells]
    j0 = row_cells[0][0]
    i0 = col_cells[0][0]

    # Start from a clean background and paint the periodic row/column
    O = [[bg for _ in range(W)] for _ in range(H)]

    if row_seq:
        L = len(row_seq)
        for j in range(W):
        O[pr][j] = row_seq[(j - j0) % L]
    if col_seq:
        L = len(col_seq)
        for i in range(H):
        O[i][pc] = col_seq[(i - i0) % L]

    return O

def p(g):
    return solve_e21d9049([row[:] for row in g])
