def solve_e509e548(I):
    from collections import Counter, deque
    G = [row[:] for row in I]
    H, W = len(G), len(G[0])

    def most_color(grid):
        return Counter([v for r in grid for v in r]).most_common(1)[0][0]

    def objects(grid):
        # 4-connected components of same color, excluding background
        bg = most_color(grid)
        seen = [[False] * W for _ in range(H)]
        out = []  # list of (color, cells)
        for i in range(H):
            for j in range(W):
                if seen[i][j]:
                    continue
                seen[i][j] = True
                c = grid[i][j]
                if c == bg:
                    continue
                q = deque([(i, j)])
                cells = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and grid[nx][ny] == c:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                            cells.append((nx, ny))
                out.append((c, cells))
        return out

    def step(grid):
        # Analyze objects on the original grid (before 3->6)
        to_two = set()
        to_one = set()
        for c, cells in objects(grid):
            if not cells:
                continue
            is_ = [i for i, _ in cells]
            js_ = [j for _, j in cells]
            min_i, max_i = min(is_), max(is_)
            min_j, max_j = min(js_), max(js_)
            h = max_i - min_i + 1
            w = max_j - min_j + 1
            # size criterion: size == h + w - 1
            if len(cells) == h + w - 1:
                to_one.update(cells)

            # inner palette contains 3 (check trimmed bbox)
            if h >= 3 and w >= 3:
                found3 = False
                for i in range(min_i + 1, max_i):
                    for j in range(min_j + 1, max_j):
                        if grid[i][j] == 3:
                            found3 = True
                            break
                    if found3:
                        break
                if found3:
                    to_two.update(cells)

        # Now replace 3 -> 6 on a copy
        g = [row[:] for row in grid]
        for i in range(H):
            for j in range(W):
                if g[i][j] == 3:
                    g[i][j] = 6

        # apply fills: TWO first, then ONE
        for i, j in to_two:
            g[i][j] = 2
        for i, j in to_one:
            g[i][j] = 1
        return g

    prev = None
    cur = [row[:] for row in G]
    for _ in range(20):
        if prev == cur:
            break
        prev = cur
        cur = step(cur)
    return cur

def p(g):
    return solve_e509e548([row[:] for row in g])
