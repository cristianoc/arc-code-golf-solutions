# ARC Task 379

def p(g):
    # Compact non - DSL solver for task 379 (ecdecbb3)
    R = range
    h, w = len(g), len(g[0])
    O = [r[:] for r in g]
    EIGHT = 8
    RED = 2
    rows = [i for i in R(h) if any(v==EIGHT for v in g[i])]
    cols = [j for j in R(w) if any(g[i][j]==EIGHT for i in R(h))]
    reds = [(i, j) for i in R(h) for j in R(w) if g[i][j]==RED]
    def square(ci, cj):
        for i in R(ci - 1, ci + 2):
        if 0<=i<h:
        for j in R(cj - 1, cj + 2):
        if 0<=j<w: O[i][j]=EIGHT
        O[ci][cj]=RED
    if len(rows)<=len(cols):
        rails = sorted(rows)
        if not rails: return O
        for i, j in reds:
        if len(rails)>=2:
        lo = max((r for r in rails if r<=i), default = None)
        up = min((r for r in rails if r>=i), default = None)
        if lo is not None and up is not None and lo!=up:
        for ii in R(lo + 2, up - 1): O[ii][j]=RED
        O[lo][j]=O[up][j]=RED
        square(lo, j)
        square(up, j)
        continue
        rr = min(rails, key = lambda r:abs(r - i))
        d = 1 if rr>i else -1
        k = i
        while True:
        nk = k + d
        if (d==1 and nk>=rr - 1) or (d==-1 and nk<=rr + 1): break
        k = nk
        O[k][j]=RED
        O[rr][j]=RED
        square(rr, j)
    else:
        rails = sorted(cols)
        if not rails: return O
        for i, j in reds:
        if len(rails)>=2:
        le = max((c for c in rails if c<=j), default = None)
        ri = min((c for c in rails if c>=j), default = None)
        if le is not None and ri is not None and le!=ri:
        for jj in R(le + 2, ri - 1): O[i][jj]=RED
        O[i][le]=O[i][ri]=RED
        square(i, le)
        square(i, ri)
        continue
        rc = min(rails, key = lambda c:abs(c - j))
        d = 1 if rc>j else -1
        k = j
        while True:
        nk = k + d
        if (d==1 and nk>=rc - 1) or (d==-1 and nk<=rc + 1): break
        k = nk
        O[i][k]=RED
        O[i][rc]=RED
        square(i, rc)
    return O
