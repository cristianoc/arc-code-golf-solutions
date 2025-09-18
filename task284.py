def solve_b7249182(I):
    # Compact non-DSL implementation preserving prior behavior.
    H, W = len(I), len(I[0])

    # Helpers
    def transpose(G):
        return tuple(map(tuple, zip(*G)))

    def mode_color(G):
        from collections import Counter
        return Counter([v for r in G for v in r]).most_common(1)[0][0]

    def bbox(cells):
        is_ = [i for i, _ in cells]
        js_ = [j for _, j in cells]
        return (min(is_), min(js_), max(is_), max(js_))

    def components(G, bg):
        h, w = len(G), len(G[0])
        seen = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if seen[i][j] or G[i][j] == bg:
                    continue
                col = G[i][j]
                q = [(i, j)]
                seen[i][j] = True
                cells = []
                while q:
                    x, y = q.pop()
                    if G[x][y] != col:
                        continue
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and G[nx][ny] == col:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                comps.append((cells, col))
        # Sort by uppermost row
        comps.sort(key=lambda t: min(i for i,_ in t[0]))
        return comps

    def connect(a, b):
        ai, aj = a; bi, bj = b
        if ai == bi:
            sj, ej = sorted((aj, bj))
            return {(ai, j) for j in range(sj, ej+1)}
        if aj == bj:
            si, ei = sorted((ai, bi))
            return {(i, aj) for i in range(si, ei+1)}
        if bi - ai == bj - aj:
            si, sj = (ai, aj) if ai <= bi else (bi, bj)
            steps = abs(bi - ai)
            return {(si + k, sj + k) for k in range(steps+1)}
        if bi - ai == aj - bj:
            si, sj = (ai, aj) if ai <= bi else (bi, bj)
            steps = abs(bi - ai)
            return {(si + k, sj - k) for k in range(steps+1)}
        return set()

    def fill(G, value, indices):
        H, W = len(G), len(G[0])
        out = [list(r) for r in G]
        for i, j in indices:
            if 0 <= i < H and 0 <= j < W:
                out[i][j] = value
        return tuple(tuple(r) for r in out)

    def paint_pairs(G, pairs):
        H, W = len(G), len(G[0])
        out = [list(r) for r in G]
        for v, (i, j) in pairs:
            if 0 <= i < H and 0 <= j < W:
                out[i][j] = v
        return tuple(tuple(r) for r in out)

    def corners(indices):
        is_ = [i for i,_ in indices]
        js_ = [j for _,j in indices]
        mi, mj, Mi, Mj = min(is_), min(js_), max(is_), max(js_)
        return (mi, mj), (mi, Mj), (Mi, mj), (Mi, Mj)

    # Normalize orientation: transpose if wider than tall considering all non-bg cells
    BG = mode_color(I)
    all_fg = [(i, j) for i in range(H) for j in range(W) if I[i][j] != BG]
    if all_fg:
        mi, mj, Mi, Mj = bbox(all_fg)
        use_identity = (Mi - mi + 1) > (Mj - mj + 1)
    else:
        use_identity = True
    G = tuple(tuple(r) for r in (I if use_identity else transpose(I)))

    # Components ordered by uppermost row
    BG_G = mode_color(G)
    comps = components(G, BG_G)
    # top and bottom objects
    (cells_top, c_top), (cells_bot, c_bot) = comps[0], comps[-1]
    # Representative coordinates (pick deterministic min to avoid randomness)
    p_top = min(cells_top)
    p_bot = min(cells_bot)

    # Vertical/straight connection and its top half
    line_tb = connect(p_top, p_bot)
    n = max(1, len(line_tb))
    si = sum(i for i, _ in line_tb) // n
    sj = sum(j for _, j in line_tb) // n
    center_pt = (si, sj)
    line_top_half = connect(p_top, center_pt)

    # Draw line: bottom color everywhere, then overwrite top half with top color
    G1 = fill(G, c_bot, line_tb)
    G2 = fill(G1, c_top, line_top_half)

    # Two-pixel vertical block at center and below
    two = {(center_pt[0], center_pt[1]), (center_pt[0] + 1, center_pt[1])}
    # Build colored pairs from current grid
    h, w = len(G2), len(G2[0])
    two_pairs = {(G2[i][j], (i, j)) for (i, j) in two if 0 <= i < h and 0 <= j < w}

    # Duplicate two-pixel object two columns left and right
    left_right = {(v, (i, j + 2)) for v, (i, j) in two_pairs} | {(v, (i, j - 2)) for v, (i, j) in two_pairs}

    # Horizontal segments above and below duplicates
    lr_indices = {(i, j) for _, (i, j) in left_right}
    if lr_indices:
        ul, ur, ll, lr = corners(lr_indices)
        top_seg = {(i-1, j) for (i, j) in connect(ul, ur)}
        bot_seg = {(i+1, j) for (i, j) in connect(ll, lr)}
    else:
        top_seg = set(); bot_seg = set()

    # Paint duplicates and border lines
    G3 = paint_pairs(G2, left_right)
    G4 = fill(G3, c_top, top_seg)
    G5 = fill(G4, c_bot, bot_seg)

    # Cover original center two cells with background
    BG2 = mode_color(G5)
    G6 = fill(G5, BG2, two)

    # Undo orientation transform
    return G6 if use_identity else transpose(G6)

def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_b7249182(G)
    return [list(r) for r in R]
