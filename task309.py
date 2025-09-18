def solve_c8f0f002(I):
    O=tuple(tuple(5 if v==7 else v for v in r) for r in I)
    return O
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_c8f0f002(G)
    return [list(r) for r in R]