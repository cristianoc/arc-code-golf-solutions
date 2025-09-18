def solve_9172f3a0(I):
    O=tuple(tuple(v for v in r for _ in range(3)) for r in I for _ in range(3))
    return O
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_9172f3a0(G)
    return [list(r) for r in R]