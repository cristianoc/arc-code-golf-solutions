F = False
T = True

ZERO = 0
ONE = 1
TWO = 2
FOUR = 4

def _components_color_4(G):
    # 4-adjacency components for color 4
    h, w = len(G), len(G[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if G[i][j] != FOUR or seen[i][j]:
                continue
            q=[(i,j)]
            seen[i][j]=True
            cur=[]
            while q:
                a,b = q.pop()
                cur.append((a,b))
                for da,db in ((1,0),(-1,0),(0,1),(0,-1)):
                    na,nb = a+da,b+db
                    if 0<=na<h and 0<=nb<w and not seen[na][nb] and G[na][nb]==FOUR:
                        seen[na][nb]=True
                        q.append((na,nb))
            comps.append(cur)
    return comps

def _inner_rect(comp):
    is_ = [i for i,_ in comp]
    js_ = [j for _,j in comp]
    top = min(is_)+1
    bot = max(is_)-1
    left = min(js_)+1
    right = max(js_)-1
    return top, left, bot, right

def solve_694f12f3(I):
    h, w = len(I), len(I[0])
    O = [list(r) for r in I]
    comps = _components_color_4(I)
    if not comps:
        return tuple(tuple(r) for r in O)
    comps_sorted = sorted(comps, key=lambda c: len(c))
    small = comps_sorted[0]
    big = comps_sorted[-1]

    # Fill small inner with ONE
    t,l,b,r = _inner_rect(small)
    if t <= b and l <= r:
        for i in range(t, b+1):
            for j in range(l, r+1):
                if 0<=i<h and 0<=j<w:
                    O[i][j] = ONE

    # Fill big inner with TWO (may overwrite)
    t,l,b,r = _inner_rect(big)
    if t <= b and l <= r:
        for i in range(t, b+1):
            for j in range(l, r+1):
                if 0<=i<h and 0<=j<w:
                    O[i][j] = TWO

    return tuple(tuple(r) for r in O)

def p(g):
    I = tuple(tuple(r) for r in g)
    R = solve_694f12f3(I)
    return [list(r) for r in R]

