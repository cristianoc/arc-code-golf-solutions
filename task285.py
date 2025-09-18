"""
Task 285 refactor: remove frozenset usage, simplify helpers,
and ensure list-of-lists output.
"""

from collections import deque, Counter
from typing import List, Tuple, Iterable, Union


Grid = List[List[int]]
Cell = Tuple[int, Tuple[int, int]]  # (value, (i,j))


def to_list_grid(g: Iterable[Iterable[int]]) -> Grid:
    return [list(row) for row in g]


def mostcolor(patch: Union[Iterable[Cell], Iterable[Iterable[int]]]) -> int:
    if not patch:
        return 0
    # Patch can be a grid or a list of colored cells
    if isinstance(patch, list) and patch and isinstance(patch[0], list):
        flat = [v for row in patch for v in row]
    else:
        flat = [v for v, _ in patch]  # type: ignore[arg-type]
    if not flat:
        return 0
    return Counter(flat).most_common(1)[0][0]


def neighbors8(i: int, j: int) -> Iterable[Tuple[int, int]]:
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            yield i + di, j + dj


def objects(grid: Grid, diagonal: bool = True, without_bg: bool = True) -> List[List[Cell]]:
    h, w = len(grid), len(grid[0])
    bg = mostcolor(grid) if without_bg else None
    seen = [[False] * w for _ in range(h)]
    objs: List[List[Cell]] = []
    get_nb = neighbors8 if diagonal else lambda i, j: ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
    for i in range(h):
        for j in range(w):
            if seen[i][j]:
                continue
            v0 = grid[i][j]
            if without_bg and v0 == bg:
                seen[i][j] = True
                continue
            comp: List[Cell] = []
            dq = deque([(i, j)])
            while dq:
                ci, cj = dq.popleft()
                if not (0 <= ci < h and 0 <= cj < w) or seen[ci][cj]:
                    continue
                v = grid[ci][cj]
                if (without_bg and v == bg):
                    seen[ci][cj] = True
                    continue
                seen[ci][cj] = True
                comp.append((v, (ci, cj)))
                for ni, nj in get_nb(ci, cj):
                    if 0 <= ni < h and 0 <= nj < w and not seen[ni][nj]:
                        # univalued=False: include any non-background cell
                        if not without_bg or grid[ni][nj] != bg:
                            dq.append((ni, nj))
            if comp:
                objs.append(comp)
    return objs


def coords(patch: Iterable[Cell]) -> List[Tuple[int, int]]:
    return [ij for _, ij in patch]


def bbox(indices: Iterable[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    ii = [i for i, _ in indices]
    jj = [j for _, j in indices]
    return min(ii), min(jj), max(ii), max(jj)






def height_width(indices: Iterable[Tuple[int, int]]) -> Tuple[int, int]:
    si, sj, ei, ej = bbox(indices)
    return (ei - si + 1, ej - sj + 1)


def center(indices: Iterable[Tuple[int, int]]) -> Tuple[int, int]:
    si, sj, ei, ej = bbox(indices)
    return (si + (ei - si) // 2, sj + (ej - sj) // 2)


def position(a_idx: Iterable[Tuple[int, int]], b_idx: Iterable[Tuple[int, int]]) -> Tuple[int, int]:
    ia, ja = center(a_idx)
    ib, jb = center(b_idx)
    if ia == ib:
        return (0, 1 if ja < jb else -1)
    if ja == jb:
        return (1 if ia < ib else -1, 0)
    if ia < ib:
        return (1, 1 if ja < jb else -1)
    if ia > ib:
        return (-1, 1 if ja < jb else -1)
    return (0, 0)


def adjacent_single_to_set(loc: Tuple[int, int], others: Iterable[Tuple[int, int]]) -> bool:
    oi, oj = loc
    other_set = set(others)
    for ni, nj in ((oi - 1, oj), (oi + 1, oj), (oi, oj - 1), (oi, oj + 1)):
        if (ni, nj) in other_set:
            return True
    return False


def hmirror_cells(patch: Iterable[Cell]) -> List[Cell]:
    idx = coords(patch)
    if not idx:
        return []
    si, sj, ei, ej = bbox(idx)
    d = si + ei
    return [(v, (d - i, j)) for v, (i, j) in patch]


def vmirror_cells(patch: Iterable[Cell]) -> List[Cell]:
    idx = coords(patch)
    if not idx:
        return []
    si, sj, ei, ej = bbox(idx)
    d = sj + ej
    return [(v, (i, d - j)) for v, (i, j) in patch]


def shift_cells(patch: Iterable[Cell], d: Tuple[int, int]) -> List[Cell]:
    di, dj = d
    return [(v, (i + di, j + dj)) for v, (i, j) in patch]


def paint(grid: Grid, cells: Iterable[Cell]) -> Grid:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for v, (i, j) in cells:
        if v != 0 and 0 <= i < h and 0 <= j < w:
            out[i][j] = v
    return out


def first_nonzero_color(grid: Grid, inter: Iterable[Tuple[int, int]]) -> int:
    # Prefer any non-zero color present at the intersection
    for i, j in inter:
        v = grid[i][j]
        if v != 0:
            return v
    # Fallback to any color (or 0 if empty)
    for i, j in inter:
        return grid[i][j]
    return 0


def solve_b775ac94(I: Iterable[Iterable[int]]) -> Grid:
    grid = to_list_grid(I)
    objs = objects(grid, diagonal=True, without_bg=True)

    out = [row[:] for row in grid]

    wave1: List[Cell] = []
    wave2: List[Cell] = []
    wave3: List[Cell] = []

    for obj in objs:
        if not obj:
            continue

        dom_color = mostcolor(obj)
        dom = [e for e in obj if e[0] == dom_color]
        rest = [e for e in obj if e[0] != dom_color]

        rest_idx = [ij for _, ij in rest]
        dom_idx = [ij for _, ij in dom]

        # Choose dominant pixel adjacent to the rest; fallback to any dominant
        chosen = None
        for e in obj:
            if e[0] != dom_color:
                continue
            if adjacent_single_to_set(e[1], rest_idx):
                chosen = e
                break
        if chosen is None:
            chosen = dom[0]

        # Rectangle covering rest ∪ {chosen}
        rect_coords = rest_idx + [chosen[1]] if rest_idx else [chosen[1]]
        si, sj, ei, ej = bbox(rect_coords)
        rect_set = {(i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1)}

        # Base shifts using relative position and object shape
        di, dj = position(dom_idx, rest_idx if rest_idx else dom_idx)
        hi, wi = height_width([ij for _, ij in obj])
        base_h = (hi * di, 0)
        base_v = (0, wi * dj)
        base_b = (hi * di, wi * dj)

        def adj(v: Tuple[int, int]) -> Tuple[int, int]:
            vi, vj = v
            def step(x: int) -> int:
                x = -x
                if x == 0:
                    return 0
                return x + 1 if x > 0 else x - 1
            return (step(vi), step(vj))

        sh_h = adj((di, 0))
        sh_v = adj((0, dj))
        sh_b = adj((di, dj))

        d1 = [e for e in shift_cells(hmirror_cells(obj), base_h) if e[0] == dom_color]
        d2 = [e for e in shift_cells(vmirror_cells(obj), base_v) if e[0] == dom_color]
        d3 = [e for e in shift_cells(hmirror_cells(vmirror_cells(obj)), base_b) if e[0] == dom_color]

        p1 = shift_cells(d1, sh_h)
        p2 = shift_cells(d2, sh_v)
        p3 = shift_cells(d3, sh_b)

        inter1 = {ij for _, ij in p1 if ij in rect_set}
        inter2 = {ij for _, ij in p2 if ij in rect_set}
        inter3 = {ij for _, ij in p3 if ij in rect_set}

        c1 = first_nonzero_color(grid, inter1)
        c2 = first_nonzero_color(grid, inter2)
        c3 = first_nonzero_color(grid, inter3)

        wave1.extend((c1, ij) for _, ij in p1)
        wave2.extend((c2, ij) for _, ij in p2)
        wave3.extend((c3, ij) for _, ij in p3)

    if wave1:
        out = paint(out, wave1)
    if wave2:
        out = paint(out, wave2)
    if wave3:
        out = paint(out, wave3)

    return out


def p(g: Iterable[Iterable[int]]) -> Grid:
    return solve_b775ac94(g)
