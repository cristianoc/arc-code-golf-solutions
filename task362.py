def solve_e48d4e1a(I):
    G = [row[:] for row in I]
    H, W = len(G), len(G[0])

    # Count number of 5s and find least frequent color after zeroing 5s
    from collections import Counter
    five_pos = [(i, j) for i in range(H) for j in range(W) if G[i][j] == 5]
    cnt5 = len(five_pos)
    tmp = [v for r in G for v in r]
    tmp = [0 if v == 5 else v for v in tmp]
    least = min(Counter(tmp).items(), key=lambda x: x[1])[0]

    # Find a cell of that color having 4 neighbors of same color (up,down,left,right)
    def has_plus(i, j):
        if G[i][j] != least:
            return False
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W and G[ni][nj] == least):
                return False
        return True

    base = None
    for i in range(H):
        for j in range(W):
            if has_plus(i, j):
                base = (i, j)
                break
        if base:
            break
    if base is None:
        # Fallback: pick any cell of that least color
        for i in range(H):
            for j in range(W):
                if G[i][j] == least:
                    base = (i, j)
                    break
            if base:
                break
        if base is None:
            return G

    ci, cj = base[0] + cnt5, base[1] - cnt5

    # Draw a cross (full row and full column) centered at (ci,cj) with color `least`
    O = [[0 for _ in range(W)] for _ in range(H)]
    if 0 <= ci < H:
        for j in range(W):
            O[ci][j] = least
    if 0 <= cj < W:
        for i in range(H):
            O[i][cj] = least

    return O

def p(g):
    return solve_e48d4e1a([row[:] for row in g])

