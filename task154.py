def p(g):
    # Move all color-5 cells into the gap between the two color-2 “U” frames.
    # If the frames are stacked vertically, compress 5-rows into that gap;
    # if side-by-side, compress 5-columns into that gap. Order is preserved.
    h = len(g)
    w = len(g[0])
    G = [row[:] for row in g]

    # Find the two connected components of color 2.
    def find_twos():
        seen = set()
        comps = []
        for i in range(h):
            for j in range(w):
                if G[i][j] == 2 and (i, j) not in seen:
                    q = [(i, j)]
                    seen.add((i, j))
                    comp = []
                    while q:
                        x, y = q.pop()
                        comp.append((x, y))
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < h and 0 <= ny < w and G[nx][ny] == 2 and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                q.append((nx, ny))
                    comps.append(comp)
        return comps

    comps = find_twos()
    if len(comps) != 2:
        return [row[:] for row in g]

    def bbox(comp):
        is_ = [i for i, _ in comp]
        js = [j for _, j in comp]
        return min(is_), min(js), max(is_), max(js)

    b0 = bbox(comps[0])
    b1 = bbox(comps[1])
    c0 = ((b0[0] + b0[2]) / 2.0, (b0[1] + b0[3]) / 2.0)
    c1 = ((b1[0] + b1[2]) / 2.0, (b1[1] + b1[3]) / 2.0)

    vertical = abs(c0[0] - c1[0]) > abs(c0[1] - c1[1])

    if vertical:
        # Gap between top and bottom frames.
        top, bot = (b0, b1) if b0[0] < b1[0] else (b1, b0)
        start = top[2] + 1
        end = bot[0] - 1
        # Collect rows that contain any 5s, preserving original order.
        above = []  # (orig_i, cols)
        inside = []
        below = []
        for i in range(h):
            cols = [j for j in range(w) if G[i][j] == 5]
            if not cols:
                continue
            if i < start:
                above.append((i, cols))
            elif i > end:
                below.append((i, cols))
            else:
                inside.append((i, cols))
        # Clear all 5s from the grid.
        for i in range(h):
            for j in range(w):
                if G[i][j] == 5:
                    G[i][j] = 0
        # Place compacted rows of 5 into the gap.
        # Fill from top with rows originally above
        i = start
        for _, cols in sorted(above, reverse=True):
            if i > end: break
            for j in cols:
                G[i][j] = 5
            i += 1
        # Keep any rows that were already inside (clamped within gap)
        for oi, cols in inside:
            if start <= oi <= end:
                for j in cols:
                    G[oi][j] = 5
        # Fill from bottom with rows originally below
        i = end
        for _, cols in sorted(below):
            if i < start: break
            for j in cols:
                G[i][j] = 5
            i -= 1
    else:
        # Gap between left and right frames.
        left, right = (b0, b1) if b0[1] < b1[1] else (b1, b0)
        start = left[3] + 1
        end = right[1] - 1
        # Collect columns that contain any 5s, preserving original order.
        left_of = []  # (orig_j, rows)
        inside = []
        right_of = []
        for j in range(w):
            rows_ = [i for i in range(h) if G[i][j] == 5]
            if not rows_:
                continue
            if j < start:
                left_of.append((j, rows_))
            elif j > end:
                right_of.append((j, rows_))
            else:
                inside.append((j, rows_))
        # Clear all 5s.
        for i in range(h):
            for j in range(w):
                if G[i][j] == 5:
                    G[i][j] = 0
        # Place compacted columns of 5 into the gap.
        # From the left side towards the gap
        j = start
        for _, rows_ in sorted(left_of, reverse=True):
            if j > end: break
            for i in rows_:
                G[i][j] = 5
            j += 1
        # Keep any columns already inside
        for oj, rows_ in inside:
            if start <= oj <= end:
                for i in rows_:
                    G[i][oj] = 5
        # From the right side towards the gap
        j = end
        for _, rows_ in sorted(right_of):
            if j < start: break
            for i in rows_:
                G[i][j] = 5
            j -= 1

    return [row[:] for row in G]
