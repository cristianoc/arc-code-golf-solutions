def p(j):
  from collections import Counter, deque
  h, w = len(j), len(j[0])

  # Background color (most common value)
  bg = Counter(v for r in j for v in r).most_common(1)[0][0]

  # Find 8-connected components of non-background cells
  vis = [[0] * w for _ in range(h)]
  comps = []  # (color, points, (top,left,bottom,right))
  for i in range(h):
    for k in range(w):
      if vis[i][k] or j[i][k] == bg:
        continue
      c = j[i][k]
      q = deque([(i, k)])
      vis[i][k] = 1
      comp = [(i, k)]
      while q:
        x, y = q.popleft()
        for dx in (-1, 0, 1):
          for dy in (-1, 0, 1):
            if dx == dy == 0:
              continue
            a, b = x + dx, y + dy
            if 0 <= a < h and 0 <= b < w and not vis[a][b] and j[a][b] == c:
              vis[a][b] = 1
              q.append((a, b))
              comp.append((a, b))
      xs = [x for x, _ in comp]
      ys = [y for _, y in comp]
      comps.append((c, comp, (min(xs), min(ys), max(xs), max(ys))))

  if not comps:
    return j

  comps.sort(key=lambda t: len(t[1]), reverse=True)
  big = comps[0]
  others = comps[1:]
  if not others:
    return j

  top, left, bot, right = big[2]
  fc = Counter(c for c, _, __ in others).most_common(1)[0][0]

  # Precompute per-row span (l,r) of the big component and its column set
  row_span = {}
  cols_big = set()
  for x, y in big[1]:
    cols_big.add(y)
    if x in row_span:
      l, r = row_span[x]
      row_span[x] = (min(l, y), max(r, y))
    else:
      row_span[x] = (y, y)

  # Columns that are background between the big's extents and their support
  gap_cols, freq = set(), {}
  for x, (l, r) in row_span.items():
    for y in range(l + 1, r):
      if j[x][y] == bg:
        gap_cols.add(y)
        freq[y] = freq.get(y, 0) + 1

  # Map each column of the big component to its occupied rows
  col_rows = {}
  for x, y in big[1]:
    col_rows.setdefault(y, []).append(x)
  for ys in col_rows.values():
    ys.sort()

  # Collect rows for the filler color in each column
  fc_cols = {}
  for c, pts, _ in others:
    if c != fc:
      continue
    for x, y in pts:
      fc_cols.setdefault(y, []).append(x)
  for ys in fc_cols.values():
    ys.sort()

  sel = []
  for col, rows in col_rows.items():
    fc_rows = fc_cols.get(col)
    if not fc_rows or fc_rows[-1] < rows[-1]:
      continue
    need = False
    prev = rows[0]
    for cur in rows[1:]:
      if cur - prev > 1:
        for r in range(prev + 1, cur):
          if j[r][col] == bg:
            need = True
            break
        if need:
          break
      prev = cur
    if not need:
      for r in range(rows[-1] + 1, h):
        if j[r][col] == bg:
          need = True
          break
    if need:
      sel.append(col)

  if not sel:
    return j

  for col in sorted(sel):
    rows = col_rows[col]
    prev = rows[0]
    for cur in rows[1:]:
      for r in range(prev + 1, cur):
        if j[r][col] == bg:
          j[r][col] = fc
      prev = cur
    for r in range(rows[-1] + 1, h):
      if j[r][col] == bg:
        j[r][col] = fc
  return j
