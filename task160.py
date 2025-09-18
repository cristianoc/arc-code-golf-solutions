# ARC Task 160

def p(j):
    h, w = len(j), len(j[0])
    from collections import Counter, deque
    bg = Counter(v for r in j for v in r).most_common(1)[0][0]
    vis = [[0]*w for _ in range(h)]
    rings = []
    to_erase = []
    for i in range(h):
    for k in range(w):
    if vis[i][k]: continue
    c = j[i][k]
    q = deque([(i, k)])
    vis[i][k]=1
    comp = []
    while q:
        x, y = q.popleft()
        comp.append((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        a, b = x + dx, y + dy
        if 0<=a<h and 0<=b<w and not vis[a][b] and j[a][b]==c:
        vis[a][b]=1
        q.append((a, b))
    if c and len(comp)==8:
        xs = [x for x, _ in comp]
        ys = [y for _, y in comp]
        if max(xs)-min(xs)==2 and max(ys)-min(ys)==2:
        rings.append((min(xs), min(ys)))
        to_erase+=comp
    for x, y in to_erase: j[x][y]=bg
    for i, jj in rings:
    x, y = i + 1, jj + 1
    for a, b in ((x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
    if 0<=a<h and 0<=b<w: j[a][b]=2
    return j
