# ARC Task 086

from typing import Tuple, List


def solve_3befdf3e(I: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    """Compact, non - DSL solver for task 086.

    For each two - color non - zero component with an inner B rectangle inside
    an A border:
    1) Expand the A border outward by the inner rectangle's size.
    2) Draw a 1 - thick B ring around the inner rectangle.
    3) Convert the inner rectangle to A.
    """
    h, w = len(I), len(I[0])
    G = [list(r) for r in I]

    # Collect 4 - connected non - zero components
    seen = [[False] * w for _ in range(h)]

    def bfs(sr: int, sc: int):
        q = [(sr, sc)]
        seen[sr][sc] = True
        cells = []
        colors = set()
        while q:
        r, c = q.pop()
        cells.append((r, c))
        colors.add(G[r][c])
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and G[nr][nc] != 0:
        seen[nr][nc] = True
        q.append((nr, nc))
        return cells, colors

    O = [row[:] for row in G]

    for i in range(h):
        for j in range(w):
        if G[i][j] != 0 and not seen[i][j]:
        comp, colors = bfs(i, j)
        if len(colors) != 2:
        continue

        rs = [r for r, _ in comp]
        cs = [c for _, c in comp]
        rmin, rmax = min(rs), max(rs)
        cmin, cmax = min(cs), max(cs)

        # Outer color A from perimeter majority
        border_vals: List[int] = []
        for r, c in comp:
        if r in (rmin, rmax) or c in (cmin, cmax):
        border_vals.append(G[r][c])
        if border_vals:
        from collections import Counter
        A = Counter(border_vals).most_common(1)[0][0]
        else:
        vals = [G[r][c] for r, c in comp]
        A = max(set(vals), key = vals.count)
        (B, ) = tuple(colors - {A})

        bpos = [(r, c) for r, c in comp if G[r][c] == B]
        if not bpos:
        continue
        brs = [r for r, _ in bpos]
        bcs = [c for _, c in bpos]
        brmin, brmax = min(brs), max(brs)
        bcmin, bcmax = min(bcs), max(bcs)
        inner_h = brmax - brmin + 1
        inner_w = bcmax - bcmin + 1
        if inner_h not in (1, 2) or inner_w not in (1, 2):
        continue

        # Expand A outward by inner size
        # Top
        top_cols = [c for c in range(cmin, cmax + 1) if (rmin, c) in comp and G[rmin][c] == A]
        for d in range(1, inner_h + 1):
        rr = rmin - d
        if rr < 0:
        break
        for c in top_cols:
        O[rr][c] = A
        # Bottom
        bot_cols = [c for c in range(cmin, cmax + 1) if (rmax, c) in comp and G[rmax][c] == A]
        for d in range(1, inner_h + 1):
        rr = rmax + d
        if rr >= h:
        break
        for c in bot_cols:
        O[rr][c] = A
        # Left
        left_rows = [r for r in range(rmin, rmax + 1) if (r, cmin) in comp and G[r][cmin] == A]
        for d in range(1, inner_w + 1):
        cc = cmin - d
        if cc < 0:
        break
        for r in left_rows:
        O[r][cc] = A
        # Right
        right_rows = [r for r in range(rmin, rmax + 1) if (r, cmax) in comp and G[r][cmax] == A]
        for d in range(1, inner_w + 1):
        cc = cmax + d
        if cc >= w:
        break
        for r in right_rows:
        O[r][cc] = A

        # 1 - thick B ring around the inner rectangle
        rr0, rr1 = brmin - 1, brmax + 1
        cc0, cc1 = bcmin - 1, bcmax + 1
        for r in range(rr0, rr1 + 1):
        for c in range(cc0, cc1 + 1):
        if 0 <= r < h and 0 <= c < w:
        on_border = (r in (rr0, rr1) or c in (cc0, cc1))
        inside_inner = (brmin <= r <= brmax and bcmin <= c <= bcmax)
        if on_border and not inside_inner:
        O[r][c] = B

        # Inner rectangle becomes A
        for r in range(brmin, brmax + 1):
        for c in range(bcmin, bcmax + 1):
        O[r][c] = A

    return tuple(tuple(row) for row in O)


def _to_list_grid(grid):
    if isinstance(grid, tuple):
        return [list(row) for row in grid]
    return grid


def p(g):
    return _to_list_grid(solve_3befdf3e(g))
