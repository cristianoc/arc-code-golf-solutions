from typing import List, Tuple

ZERO = 0
FIVE = 5


def solve_a78176bb(I: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    # Choose drawing color: any non-zero, non-FIVE color present (fallback to FIVE)
    colors = set(v for row in I for v in row)
    draw_color = next((c for c in colors if c != ZERO and c != FIVE), FIVE)

    h, w = len(I), len(I[0])

    # Find 4-connected components of FIVE
    visited = [[False] * w for _ in range(h)]
    comps = []  # list of lists of (i,j)

    for i in range(h):
        for j in range(w):
            if I[i][j] != FIVE or visited[i][j]:
                continue
            stack = [(i, j)]
            visited[i][j] = True
            comp = []
            while stack:
                ci, cj = stack.pop()
                comp.append((ci, cj))
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and I[ni][nj] == FIVE:
                        visited[ni][nj] = True
                        stack.append((ni, nj))
            comps.append(comp)

    # For each FIVE-component, select start point just outside UR or LL corner
    starts = []  # list of (i,j)
    for comp in comps:
        min_i = min(i for i, _ in comp)
        max_i = max(i for i, _ in comp)
        min_j = min(j for _, j in comp)
        max_j = max(j for _, j in comp)
        # If UR corner is FIVE in the grid, extend from just outside UR; otherwise from LL
        if 0 <= min_i < h and 0 <= max_j < w and I[min_i][max_j] == FIVE:
            starts.append((min_i - 1, max_j + 1))
        else:
            starts.append((max_i + 1, min_j - 1))

    # Draw slope +1 diagonals (i - j constant) through each start point
    to_fill = set()
    for si, sj in starts:
        c = si - sj
        for i in range(h):
            j = i - c
            if 0 <= j < w:
                to_fill.add((i, j))

    # Produce output: paint those positions with draw_color, then remove all FIVE (set to ZERO)
    out = [list(row) for row in I]
    for i, j in to_fill:
        out[i][j] = draw_color
    for i in range(h):
        for j in range(w):
            if out[i][j] == FIVE:
                out[i][j] = ZERO
    return tuple(tuple(row) for row in out)


def p(g: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in solve_a78176bb(tuple(tuple(row) for row in g))]

