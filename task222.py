# ARC Task 222

def p(g, L = len, R = range):
    h, w = L(g), L(g[0])
    best = (0, 0, 0, 0, 0) # area, r0, r1, c0, c1
    color stored via area sign trick
    for col in R(1, 10):
    H = [0]*w
    for r in R(h):
    for c in R(w): H[c]=H[c]+1 if g[r][c]==col else 0
    st = []
    for c in R(w + 1):
    cur = H[c] if c<w else 0
    last = c
    while st and st[-1][0]>cur:
    hgt, pos = st.pop()
    area = hgt*(c - pos)
    # pack color by adding a tiny epsilon via tuple order
    if area>best[0]: best = (area, r - hgt + 1, r, pos, c - 1, col)
    last = pos
    st.append((cur, last))
    # Build output
    if best[0]==0:
    return [[0]*w for _ in R(h)]
    _, r0, r1, c0, c1, col = best
    o = [[0]*w for _ in R(h)]
    for r in R(r0, r1 + 1):
    for c in R(c0, c1 + 1): o[r][c]=col
    return o
