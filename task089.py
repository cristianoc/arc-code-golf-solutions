# ARC Task 089

"""Task 089: Compact non - DSL solution for ARC task 3e980e27.

Behavior summary:
- Find diagonal - connected objects of non - background pixels.
- For color 2 and color 3 separately:
    - Take the largest object that contains that color, vertically mirror it,
    and normalize it so the upper - left of that color's pixels is at (0, 0).
    - Paste this template at the center of every other object that contains
    that color.
- Paint all pasted templates onto the original grid.
"""

from collections import deque
from typing import Iterable, List, Tuple

Grid = Tuple[Tuple[int, ...], ...]
Pixel = Tuple[int, Tuple[int, int]]
Object = Tuple[Pixel, ...]


def mostcolor(grid: Grid) -> int:
    counts = {}
    for row in grid:
        for v in row:
        counts[v] = counts.get(v, 0) + 1
    return max(counts, key = counts.get)


def neighbors8(i: int, j: int) -> Iterable[Tuple[int, int]]:
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        yield i + di, j + dj


def objects_diag_nonbg(grid: Grid) -> List[Object]:
    h, w = len(grid), len(grid[0])
    bg = mostcolor(grid)
    visited = [[False] * w for _ in range(h)]
    objs: List[Object] = []
    for i in range(h):
        for j in range(w):
        if visited[i][j] or grid[i][j] == bg:
        continue
        comp: List[Pixel] = []
        q = deque([(i, j)])
        visited[i][j] = True
        while q:
        ci, cj = q.popleft()
        comp.append((grid[ci][cj], (ci, cj)))
        for ni, nj in neighbors8(ci, cj):
        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] != bg:
        visited[ni][nj] = True
        q.append((ni, nj))
        objs.append(tuple(comp))
    return objs


def palette(obj: Object) -> set:
    return {v for v, _ in obj}


def bbox_indices(indices: Iterable[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    indices = list(indices)
    is_ = [i for i, _ in indices]
    js_ = [j for _, j in indices]
    return min(is_), min(js_), max(is_), max(js_)


def ul_lr(obj: Object) -> Tuple[int, int, int, int]:
    return bbox_indices(pos for _, pos in obj)


def vmirror(obj: Object) -> Object:
    # Mirror across vertical axis of the object's bounding box
    _, jmin, _, jmax = ul_lr(obj)
    d = jmin + jmax
    return tuple((v, (i, d - j)) for v, (i, j) in obj)


def shift_obj(obj: Object, delta: Tuple[int, int]) -> Object:
    di, dj = delta
    return tuple((v, (i + di, j + dj)) for v, (i, j) in obj)


def center(obj: Object) -> Tuple[int, int]:
    imin, jmin, imax, jmax = ul_lr(obj)
    return (imin + (imax - imin) // 2, jmin + (jmax - jmin) // 2)


def paint(grid: Grid, obj_pixels: Iterable[Pixel]) -> Grid:
    h, w = len(grid), len(grid[0])
    out = [list(row) for row in grid]
    for v, (i, j) in obj_pixels:
        if 0 <= i < h and 0 <= j < w:
        out[i][j] = v
    return tuple(tuple(row) for row in out)


def normalize_template_by_color(obj: Object, color: int) -> Object | None:
    # Shift so the UL corner of the subset with the given color is at (0, 0)
    indices = [pos for v, pos in obj if v == color]
    if not indices:
        return None
    imin, jmin, _, _ = bbox_indices(indices)
    return shift_obj(obj, (-imin, -jmin))


def solve_3e980e27(I: Grid) -> Grid:
    objs = objects_diag_nonbg(I)

    placements: List[Pixel] = []
    for color in (2, 3):
        group = [o for o in objs if color in palette(o)]
        if len(group) <= 1:
        continue
        largest = max(group, key = len)
        source = vmirror(largest) if color == 2 else largest
        template = normalize_template_by_color(source, color)
        if template is None:
        continue
        for o in group:
        if o is largest:
        continue
        ci, cj = center(o)
        placements.extend(shift_obj(template, (ci, cj)))

    O = paint(I, placements)
    return O


def _to_list_grid(grid):
    if isinstance(grid, tuple):
        return [list(row) for row in grid]
    return grid


def p(g):
    return _to_list_grid(solve_3e980e27(g))
