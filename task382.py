ZERO = 0
TWO = 2
EIGHT = 8

def _ofcolor(G, c):
    return {(i, j) for i, row in enumerate(G) for j, v in enumerate(row) if v == c}

def _bbox_rows_cols(cells):
    is_ = [i for i, _ in cells]
    js_ = [j for _, j in cells]
    return (min(is_), max(is_), min(js_), max(js_))


def _vmirror(G):
    return tuple(tuple(reversed(row)) for row in G)

def _hmirror(G):
    return tuple(reversed(G))

def _dmirror(G):
    return tuple(tuple(row) for row in zip(*G))

def _fill(G, val, cells):
    h, w = len(G), len(G[0])
    O = [list(r) for r in G]
    for i, j in cells:
        if 0 <= i < h and 0 <= j < w:
            O[i][j] = val
    return tuple(tuple(r) for r in O)

def solve_f15e1fac(I):
    G = tuple(tuple(r) for r in I)

    # 1) normalize orientation via diagonal mirror so that EIGHTs lie horizontally (not vertically)
    eight_I = _ofcolor(G, EIGHT)
    if eight_I:
        er1, er2, ec1, ec2 = _bbox_rows_cols(eight_I)
        # transpose when EIGHT cluster is taller than wide
        use_d = (er2 - er1 + 1) > (ec2 - ec1 + 1)
    else:
        use_d = False
    X = _dmirror(G) if use_d else G

    # 2) ensure TWO is at left border by vertical mirror if needed (on current X)
    two_X = _ofcolor(X, TWO)
    leftmost_two = min((j for _, j in two_X), default=0)
    use_v = leftmost_two != 0
    X = _vmirror(X) if use_v else X

    # 3) ensure EIGHT touches top by horizontal mirror if needed (on current X)
    eight_X = _ofcolor(X, EIGHT)
    top_eight = min((i for i, _ in eight_X), default=0)
    use_h = (top_eight != 0)
    X = _hmirror(X) if use_h else X

    h, w = len(X), len(X[0])

    # Rays: for every 8, include all cells straight downwards within grid
    rays = set()
    for i, j in _ofcolor(X, EIGHT):
        for r in range(i, h):
            rays.add((r, j))

    # Intervals between rows containing TWO (distinct rows), bounded by 0 and h-1
    two_rows = sorted({i for i, _ in _ofcolor(X, TWO)})
    starts = [0] + two_rows
    ends = [r - 1 for r in two_rows] + [h - 1]
    intervals = list(zip(starts, ends))

    # For each interval k, take ray points with row in [start, end] and shift right by k
    paint = set()
    for k, (a, b) in enumerate(intervals):
        for i, j in rays:
            if a <= i <= b:
                paint.add((i, j + k))

    Y = _fill(X, EIGHT, paint)

    # Undo transforms in reverse order
    if use_h:
        Y = _hmirror(Y)
    if use_v:
        Y = _vmirror(Y)
    if use_d:
        Y = _dmirror(Y)
    return Y

def p(g):
    try:
        G = tuple(tuple(r) for r in g)
        R = solve_f15e1fac(G)
        return [list(r) for r in R]
    except Exception:
        return [list(row) for row in g]
