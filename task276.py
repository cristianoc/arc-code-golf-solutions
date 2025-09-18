def solve_b1948b0a(I):
    O=tuple(tuple(2 if v==6 else v for v in r) for r in I)
    return O
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_b1948b0a(G)
    return [list(r) for r in R]