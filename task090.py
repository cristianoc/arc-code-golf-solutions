# ARC Task 090

def p(g):
    I = [r[:] for r in g]
    H, W = len(I), len(I[0])
    best = None
    bsz = -1
    for h in range(2, min(9, H)+1):
        for w in range(2, min(9, W)+1):
        for i in range(0, H - h + 1):
        for j in range(0, W - w + 1):
        ok = True
        for a in range(i, i + h):
        row = I[a]
        if any(row[b]!=0 for b in range(j, j + w)):
        ok = False
        break
        if ok and h * w>bsz:
        bsz = h * w
        best = (i, j, h, w)
    if best:
        i, j, h, w = best
        for a in range(i, i + h):
        for b in range(j, j + w):
        I[a][b]=6
    return I
