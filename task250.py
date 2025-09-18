# ARC Task 250

def p(g):
    I = [r[:] for r in g]
    H, W = len(I), len(I[0])
    twos = [(i, j) for i in range(H) for j in range(W) if I[i][j]==2]
    fives = [(i, j) for i in range(H) for j in range(W) if I[i][j]==5]
    if not twos or not fives: return I
    # outbox (perimeter around bbox of all 2s)
    ti = min(i for i, _ in twos)
    tj = min(j for _, j in twos)
    bi = max(i for i, _ in twos)
    bj = max(j for _, j in twos)
    per = set()
    for j in range(max(0, tj - 1), min(W, bj + 2)):
        if 0<=ti - 1<H: per.add((ti - 1, j))
        if 0<=bi + 1<H: per.add((bi + 1, j))
    for i in range(max(0, ti - 1), min(H, bi + 2)):
        if 0<=tj - 1<W: per.add((i, tj - 1))
        if 0<=bj + 1<W: per.add((i, bj + 1))
    per = list(per)
    # nearest perimeter point for each 5 (Manhattan)
    def nearest(i, j):
        best = None
        bd = 10**9
        for a, b in per:
        d = abs(a - i)+abs(b - j)
        if d<bd: bd = d
        best = (a, b)
        return best
    targets = set(nearest(i, j) for i, j in fives if nearest(i, j))
    # cover original 5s with bg
    from collections import Counter
    vals = [v for r in I for v in r]
    bg = max(Counter(vals), key = Counter(vals).get)
    for i, j in fives: I[i][j]=bg
    # fill targets with 5
    for a, b in targets: I[a][b]=5
    return I
