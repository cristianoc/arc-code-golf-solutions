# ARC Task 221

def p(g):
    """Compact, non - DSL implementation for task 221 (91413438).

    Steps (preserving original behavior):
    - Count zeros z in input 3xW grid.
    - Create an extension of width 3 * z*z - 3 filled with 0s and append to the right.
    - Find the first 8 - connected non - background component (background = most common color).
    - Paint copies of that component every 3 columns to the right, for (9 - z) copies.
    - Horizontally split the result into z equal - width slices (with the same offset rule),
    then stack those slices vertically.
    """
    try:
        # Normalize input to list - of - lists
        G = [row[:] for row in g]
        h, w = len(G), len(G[0]) if G else 0

        # 1) Count zeros in the original input
        z = sum(v == 0 for row in G for v in row)

        # 2) Extend canvas to the right by 3 * z*z - 3 columns of zeros
        ext_w = 3 * z * z - 3
        if ext_w > 0:
        for i in range(h):
        G[i] = G[i] + [0] * ext_w

        H, W = h, (w + max(0, ext_w))

        # 3) Determine background as the most frequent color in the extended grid
        flat = [v for row in G for v in row]
        if not flat:
        return [list(r) for r in g]
        # Most frequent color
        bg = max(set(flat), key = flat.count)

        # 4) Find the first 8 - connected non - background component in row - major order
        visited = [[False] * W for _ in range(H)]
        base_cells = []  # (i, j, color)

        def neighbors8(i: int, j: int):
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
        yield ni, nj

        # Collect ALL univalued 8 - connected non - bg components in row - major order
        components: list[list[tuple[int, int, int]]] = []
        for i in range(H):
        for j in range(W):
        if G[i][j] == bg or visited[i][j]:
        continue
        col = G[i][j]
        stack = [(i, j)]
        visited[i][j] = True
        comp_cells: list[tuple[int, int, int]] = []
        while stack:
        ci, cj = stack.pop()
        comp_cells.append((ci, cj, col))
        for ni, nj in neighbors8(ci, cj):
        if not visited[ni][nj] and G[ni][nj] != bg and G[ni][nj] == col:
        visited[ni][nj] = True
        stack.append((ni, nj))
        components.append(comp_cells)

        if not components:
        return [row[:] for row in G]

        # 5) Paint shifted copies every 3 columns for (9 - z) copies, for all components
        copies = max(0, 9 - z)
        for k in range(copies):
        shift_j = 3 * k
        for comp in components:
        for ci, cj, col in comp:
        tj = cj + shift_j
        if 0 <= tj < W:
        G[ci][tj] = col

        # 6) Split into z vertical slices (like the original hsplit) and stack vertically
        if z <= 0:
        return [row[:] for row in G]
        slice_w = W // z
        offset = 1 if (W % z) != 0 else 0
        parts = []
        for idx in range(z):
        start = slice_w * idx + idx * offset
        sub = [r[start:start + slice_w] for r in G]
        parts.append(sub)
        # Stack all parts vertically
        out = [row for part in parts for row in part]
        return out
    except Exception:
        # Fail - safe behavior matching original wrapper
        return [list(r) for r in g]
