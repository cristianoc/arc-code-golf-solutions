# ARC Task 240

from collections import Counter


def _build_coarse(grid):
    """Collapse odd - index cells into a coarse grid with axial symmetry copies."""
    h = len(grid)
    w = len(grid[0]) if h else 0
    if h < 3 or w < 3 or (h - 1) % 2 or (w - 1) % 2:
        return None
    hc = (h - 1) // 2
    wc = (w - 1) // 2
    coarse = [[0] * wc for _ in range(hc)]
    for r in range(1, h, 2):
        for c in range(1, w, 2):
        v = grid[r][c]
        if not v:
        continue
        rr = (r - 1) // 2
        cc = (c - 1) // 2
        for R in {rr, hc - 1 - rr}:
        for C in {cc, wc - 1 - cc}:
        coarse[R][C] = v
    return coarse


def _pick_edge_color(coarse):
    if coarse is None:
        return None
    hc = len(coarse)
    wc = len(coarse[0])
    corner = coarse[0][0]
    info = {}
    for r in range(hc):
        for c in range(wc):
        v = coarse[r][c]
        if v == 0 or v == corner:
        continue
        rec = info.setdefault(v, [0, False, False, False, False])
        rec[0] += 1
        if r == 0:
        rec[1] = True
        if c == 0:
        rec[2] = True
        if r == 1:
        rec[3] = True
        if c == 1:
        rec[4] = True
    eligible = {v: rec for v, rec in info.items() if rec[0] >= 8}
    if not eligible:
        return None
    top = [
        (v, rec)
        for v, rec in eligible.items()
        if rec[1] or rec[2]
    ]
    if top:
        return max(top, key = lambda item: (item[1][0], -item[0]))[0]
    near = [
        (v, rec)
        for v, rec in eligible.items()
        if rec[3] or rec[4]
    ]
    if near:
        return max(near, key = lambda item: (item[1][0], -item[0]))[0]
    return None


def _fill_segments(coarse, edge):
    if coarse is None:
        return None
    hc = len(coarse)
    wc = len(coarse[0])
    counts = Counter(v for row in coarse for v in row if v)
    colors = [v for v, cnt in counts.items() if cnt >= 8]
    out = [row[:] for row in coarse]

    for color in colors:
        # Horizontal gaps
        for r in range(hc):
        row = coarse[r]
        anchors = [c for c, v in enumerate(row) if v == color]
        if len(anchors) < 2:
        continue
        if color == edge:
        if not any(v not in (0, edge) for v in row):
        continue
        else:
        if not any(v not in (0, edge, color) for v in row):
        continue
        for c1, c2 in zip(anchors, anchors[1:]):
        if c1 == 0 and c2 == wc - 1:
        continue
        if any(coarse[r][c] != 0 for c in range(c1 + 1, c2)):
        continue
        for c in range(c1 + 1, c2):
        if out[r][c] == 0:
        out[r][c] = color

        # Vertical gaps
        for c in range(wc):
        col = [coarse[r][c] for r in range(hc)]
        anchors = [r for r, v in enumerate(col) if v == color]
        if len(anchors) < 2:
        continue
        if color == edge:
        if not any(v not in (0, edge) for v in col):
        continue
        else:
        if not any(v not in (0, edge, color) for v in col):
        continue
        for r1, r2 in zip(anchors, anchors[1:]):
        if r1 == 0 and r2 == hc - 1:
        continue
        if any(coarse[r][c] != 0 for r in range(r1 + 1, r2)):
        continue
        for r in range(r1 + 1, r2):
        if out[r][c] == 0:
        out[r][c] = color

    return out


def _expand_to_full(coarse, height, width):
    out = [[0] * width for _ in range(height)]
    if coarse is None:
        return out
    for r, row in enumerate(coarse):
        for c, v in enumerate(row):
        if v:
        out[2 * r + 1][2 * c + 1] = v
    return out


def solve_9d9215db(I):
    grid = [list(row) for row in I]
    H = len(grid)
    W = len(grid[0]) if H else 0
    coarse = _build_coarse(grid)
    if coarse is None:
        return I
    edge = _pick_edge_color(coarse)
    filled = _fill_segments(coarse, edge)
    out = _expand_to_full(filled, H, W)
    return tuple(tuple(row) for row in out)


def p(g):
    try:
        I = tuple(tuple(row) for row in g)
        out = solve_9d9215db(I)
        if isinstance(out, tuple):
        return [list(r) for r in out]
        if isinstance(out, list) and all(isinstance(r, list) for r in out):
        return out
        return [list(r) for r in g]
    except Exception:
        return [list(r) for r in g]
