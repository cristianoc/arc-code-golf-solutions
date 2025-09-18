def solve_db93a21d(I):
    G = [row[:] for row in I]
    H, W = len(G), len(G[0])

    # Background color = most frequent
    from collections import Counter, deque
    bg = Counter([v for r in G for v in r]).most_common(1)[0][0]

    # 8-connected components by same color
    seen = [[False] * W for _ in range(H)]
    comps = []  # list of (color, [(i,j)])
    for i in range(H):
        for j in range(W):
            if seen[i][j]:
                continue
            seen[i][j] = True
            c = G[i][j]
            if c == bg:
                continue
            q = deque([(i, j)])
            cells = [(i, j)]
            while q:
                x, y = q.popleft()
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and G[nx][ny] == c:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                            cells.append((nx, ny))
            comps.append((c, cells))

    # Underfill: from every 9, shoot downward and set bg cells to 1
    for i in range(H):
        for j in range(W):
            if G[i][j] == 9:
                for r in range(i, H):
                    if G[r][j] == bg:
                        G[r][j] = 1

    # For each color-9 component, draw a green (3) frame of thickness width//2 around its bbox
    for c, cells in comps:
        if c != 9 or not cells:
            continue
        min_i = min(i for i, _ in cells)
        max_i = max(i for i, _ in cells)
        min_j = min(j for _, j in cells)
        max_j = max(j for _, j in cells)
        k = (max_j - min_j + 1) // 2
        for t in range(1, k + 1):
            top, bot = min_i - t, max_i + t
            left, right = min_j - t, max_j + t
            # horizontal edges
            if 0 <= top < H:
                for y in range(max(0, left), min(W, right + 1)):
                    G[top][y] = 3
            if 0 <= bot < H:
                for y in range(max(0, left), min(W, right + 1)):
                    G[bot][y] = 3
            # vertical edges
            if 0 <= left < W:
                for x in range(max(0, top), min(H, bot + 1)):
                    G[x][left] = 3
            if 0 <= right < W:
                for x in range(max(0, top), min(H, bot + 1)):
                    G[x][right] = 3

    return G

def p(g):
    return solve_db93a21d([row[:] for row in g])

