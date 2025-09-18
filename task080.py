from collections import Counter


def solve_39e1d7f9(I):
    if not I:
        return tuple()

    H = len(I)
    W = len(I[0])
    G = [list(row) for row in I]

    def uniform_rows_cols() -> tuple[list[int], list[int]]:
        rows = [i for i in range(H) if all(cell == G[i][0] for cell in G[i])]
        cols = [j for j in range(W) if all(G[i][j] == G[0][j] for i in range(H))]
        return rows, cols

    def slice_bounds(uniform: list[int], limit: int) -> list[tuple[int, int]]:
        res: list[tuple[int, int]] = []
        prev = -1
        for idx in uniform:
            if idx - (prev + 1) > 0:
                res.append((prev + 1, idx))
            prev = idx
        if prev < limit - 1:
            res.append((prev + 1, limit))
        return res

    uniform_rows, uniform_cols = uniform_rows_cols()
    if not uniform_rows or not uniform_cols:
        return tuple(tuple(row) for row in G)

    row_bounds = slice_bounds(uniform_rows, H)
    col_bounds = slice_bounds(uniform_cols, W)
    if not row_bounds or not col_bounds:
        return tuple(tuple(row) for row in G)

    R = len(row_bounds)
    C = len(col_bounds)
    block = [[G[row_bounds[i][0]][col_bounds[j][0]] for j in range(C)] for i in range(R)]

    flat = [block[i][j] for i in range(R) for j in range(C)]
    bg = Counter(flat).most_common(1)[0][0]

    template: list[list[int]] | None = None
    center_color = None
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            center = block[i][j]
            if center == bg:
                continue
            left = block[i][j - 1]
            right = block[i][j + 1]
            up = block[i - 1][j]
            down = block[i + 1][j]
            if left == right and up == down and (left != bg or up != bg):
                template = [[block[i + di - 1][j + dj - 1] for dj in range(3)] for di in range(3)]
                center_color = center
                break
        if template is not None:
            break

    if template is None or center_color is None:
        return tuple(tuple(row) for row in G)

    new_block = [row[:] for row in block]
    for i in range(R):
        for j in range(C):
            if block[i][j] == center_color:
                for di in (-1, 0, 1):
                    ni = i + di
                    if 0 <= ni < R:
                        for dj in (-1, 0, 1):
                            nj = j + dj
                            if 0 <= nj < C:
                                new_block[ni][nj] = template[di + 1][dj + 1]

    for bi, (r0, r1) in enumerate(row_bounds):
        for bj, (c0, c1) in enumerate(col_bounds):
            val = new_block[bi][bj]
            for r in range(r0, r1):
                G[r][c0:c1] = [val] * (c1 - c0)

    return tuple(tuple(row) for row in G)


def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_39e1d7f9(G)
    return [list(r) for r in R]
