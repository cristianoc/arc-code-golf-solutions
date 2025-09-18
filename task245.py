# ARC Task 245

def p(g):
    I = [r[:] for r in g]
    H, W = len(I), len(I[0])
    # collect positions of color 2 and 3
    twos = [(i, j) for i in range(H) for j in range(W) if I[i][j]==2]
    threes = [(i, j) for i in range(H) for j in range(W) if I[i][j]==3]
    if not twos or not threes: return I
    # compute offset = ulcorner(three) - ulcorner(two) + (1, 1)
    t2i = min(i for i, _ in twos)
    t2j = min(j for _, j in twos)
    t3i = min(i for i, _ in threes)
    t3j = min(j for _, j in threes)
    di = (t3i - t2i) + 1
    dj = (t3j - t2j) + 1
    # background color (most frequent)
    from collections import Counter
    vals = [v for r in I for v in r]
    bg = max(Counter(vals), key = Counter(vals).get)
    # cover originals where 2s were
    for i, j in twos:
        I[i][j]=bg
    # paint moved 2s
    for i, j in twos:
        a, b = i + di, j + dj
        if 0<=a<H and 0<=b<W: I[a][b]=2
    return I
