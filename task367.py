# ARC Task 367

def solve_e73095fd(I):
    H, W = len(I), len(I[0])

    def objects_by_color(grid, color):
        seen = [[False]*W for _ in range(H)]
        out = []
        for i in range(H):
        for j in range(W):
        if seen[i][j]:
        continue
        seen[i][j] = True
        if grid[i][j] != color:
        continue
        q = [(i, j)]
        qi = 0
        comp = [(i, j)]
        while qi < len(q):
        x, y = q[qi]
        qi += 1
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny]:
        seen[nx][ny] = True
        if grid[nx][ny] == color:
        q.append((nx, ny))
        comp.append((nx, ny))
        out.append(comp)
        return out

    def bbox(cells):
        is_ = [i for i, _ in cells]
        js_ = [j for _, j in cells]
        return min(is_), min(js_), max(is_), max(js_)

    def is_full_rectangle(cells):
        u, l, d, r = bbox(cells)
        area = (d - u + 1)*(r - l + 1)
        return len(cells) == area

    def outbox(cells):
        u, l, d, r = bbox(cells)
        si, sj = u - 1, l - 1
        ei, ej = d + 1, r + 1
        vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
        hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
        return vlines | hlines

    def corners(rect):
        u, l, d, r = bbox(list(rect))
        return {(u, l), (u, r), (d, l), (d, r)}

    # collect all color - 5 indices once
    fives = {(i, j) for i in range(H) for j in range(W) if I[i][j] == 5}

    to_fill = set()
    for comp in objects_by_color(I, 0):
        if not is_full_rectangle(comp):
        continue
        ob = outbox(comp)
        # neighbors of corners of outbox
        neigh = set()
        for x, y in corners(ob):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        neigh.add((nx, ny))
        # remove the outbox itself
        neigh -= ob
        # if no color - 5 adjacent in these positions -> select
        if fives.isdisjoint(neigh):
        to_fill.update(comp)

    G = [list(row) for row in I]
    for i, j in to_fill:
        if 0 <= i < H and 0 <= j < W:
        G[i][j] = 4
    return tuple(tuple(r) for r in G)

def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_e73095fd(G)
    return [list(r) for r in R]
