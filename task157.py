# ARC Task 157

def p(g):
    """Task 157 solution without frozenset.

    - Finds connected components of non - zero cells (4 - neighborhood).
    - Optionally repositions non - largest components subject to constraints.
    - Always returns a list - of - lists grid
    maps 5 -> 0 in the working grid.
    """

    h, w = len(g), len(g[0])

    # Build connected components (4 - neighborhood) of non - zero cells
    seen = [[False] * w for _ in range(h)]
    comps = []

    for i in range(h):
        for j in range(w):
        if g[i][j] and not seen[i][j]:
        # BFS from (i, j)
        q = [(i, j)]
        seen[i][j] = True
        comp = set()
        while q:
        x, y = q.pop()
        comp.add((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and g[nx][ny]:
        seen[nx][ny] = True
        q.append((nx, ny))
        comps.append(comp)

    if not comps:
        # No non - zero cells; return a deep copy with 5 -> 0 mapping
        return [[0 if v == 5 else v for v in row] for row in g]

    # Order components by size; keep only the non - largest for potential moves
    others = sorted(comps, key = len, reverse = True)[1:]

    # Working grid: replace 5 with 0 (original used eval(str(g)).replace('5', '0'))
    grid = [[0 if v == 5 else v for v in row] for row in g]

    # Helper to collect coordinates for a color
    def coords_of(color):
        return {(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == color}

    background = coords_of(0)
    # Walls are color 2 plus virtual left/right borders on rows 0..2
    walls = coords_of(2) | {(i, -1) for i in (0, 1, 2)} | {(i, w) for i in (0, 1, 2)}

    # Move each non - main component
    for comp in others:
        # Normalize comp to top - left origin
        min_i = min(i for i, _ in comp)
        min_j = min(j for _, j in comp)
        shape = {(i - min_i, j - min_j) for i, j in comp}

        def shifted(pos):
        x0, y0 = pos
        return {(i + x0, j + y0) for i, j in shape}

        def neighbor_cells(cells):
        return {
        (x + a, y + b)
        for x, y in cells
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0))
        }

        def score(pos):
        return len(walls & neighbor_cells(shifted(pos)))

        # Candidate placements: only rows 1 or 2, any column
        candidates = {(x, y) for x in (1, 2) for y in range(w)}

        def valid(pos):
        placed = shifted(pos)
        # Must fit in background, avoid walls
        if not placed.issubset(background):
        return False
        if placed & walls:
        return False
        # Additional constraint mirroring the original logic
        neigh = (background & neighbor_cells(placed)) - placed
        if not neigh:
        return False
        min_row = min(i for i, _ in neigh)
        return min_row > 2

        feasible = list(filter(valid, candidates))
        if not feasible:
        # Nothing sensible; skip moving this component
        continue

        x, y = max(feasible, key = score)
        for i, j in shape:
        xi, yj = i + x, j + y
        if 0 <= xi < h and 0 <= yj < w:
        grid[xi][yj] = 1

    return grid
