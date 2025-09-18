# ARC Task 105

from typing import List

Grid = List[List[int]]


def p(grid: Grid) -> Grid:
    """
    Rectangle + single - beam solver for ARC task 105.

    - Find the bounding rectangle of all blue (1) cells.
    - Perimeter fill: set every 0 on the rectangle border to red (2).
    - Pick exactly one beam (a full row or column inside the rectangle) to fill,
    using only INTERIOR cells to decide eligibility and priority:
        * The beam must have at least one interior zero and at least one interior
        filled cell (1 or 2).
        * It must NOT intersect any complete orthogonal beam, where completeness
        is defined over interior cells (all interior cells are non - zero).
        * Among eligible beams, choose the one with the most interior filled
        cells
        fill its zeros with 2.
    """
    h = len(grid)
    if h == 0:
        return grid
    w = len(grid[0])
    out = [row[:] for row in grid]

    # 1) Bounding rectangle of blue cells
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    if not ones:
        return out

    min_r = min(r for r, _ in ones)
    max_r = max(r for r, _ in ones)
    min_c = min(c for _, c in ones)
    max_c = max(c for _, c in ones)

    # 2) Perimeter fill only: Ensure the rectangle border has no zeros. Fill any 0 on the
    # rectangle border with red (keep 1s untouched).
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
        if r in (min_r, max_r) or c in (min_c, max_c):
        if out[r][c] == 0:
        out[r][c] = 2

    # 3) Beam selection helpers
    def beams():
        for rr in range(min_r, max_r + 1):
        yield [(rr, cc) for cc in range(min_c, max_c + 1)]
        for cc in range(min_c, max_c + 1):
        yield [(rr, cc) for rr in range(min_r, max_r + 1)]

    def is_interior(r: int, c: int) -> bool:
        return (min_r < r < max_r) and (min_c < c < max_c)

    # (no gap computation needed for the final rule set)

    # Single - beam fill: choose one eligible beam and fill it once, then stop.
    # Determine complete orthogonal beams based on INTERIOR cells only
    # (edges are ignored for this decision).
    complete_rows = set()
    if max_c - min_c >= 2:  # has interior columns
        for rr in range(min_r, max_r + 1):
        if all(out[rr][cc] != 0 for cc in range(min_c + 1, max_c)):
        complete_rows.add(rr)
    complete_cols = set()
    if max_r - min_r >= 2:  # has interior rows
        for cc in range(min_c, max_c + 1):
        if all(out[rr][cc] != 0 for rr in range(min_r + 1, max_r)):
        complete_cols.add(cc)

    def intersects_complete_orthogonal(beam_cells):
        # Intersection test is also restricted to INTERIOR crossing points.
        if not beam_cells:
        return False
        is_row = True
        for i in range(1, len(beam_cells)):
        if beam_cells[i][0] != beam_cells[0][0]:
        is_row = False
        break
        if is_row:
        return any((min_c < c < max_c) and (c in complete_cols) for _, c in beam_cells)
        else:
        return any((min_r < r < max_r) and (r in complete_rows) for r, _ in beam_cells)

    best = None
    best_occ = -1
    for beam in beams():
        # Consider INTERIOR portion of the beam only
        interior_cells = [(r, c) for r, c in beam if is_interior(r, c)]
        if not interior_cells:
        # No interior at all; skip per expected behavior
        continue
        occ = sum(1 for r, c in interior_cells if out[r][c] != 0)
        zeros = sum(1 for r, c in interior_cells if out[r][c] == 0)
        # New rule: fill a beam only if it does NOT intersect another
        # complete orthogonal beam, and it has interior zeros to fill.
        if zeros == 0:
        continue
        if occ < 1:
        continue
        if intersects_complete_orthogonal(beam):
        continue
        # Prioritize beam with the most already filled INTERIOR cells
        if occ > best_occ:
        best_occ = occ
        best = beam
    if best is not None:
        for r, c in best:
        if out[r][c] == 0:
        out[r][c] = 2

    return out
