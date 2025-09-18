def solve_6150a2bd(I):
    O=tuple(tuple(reversed(r)) for r in I[::-1])
    return O
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_6150a2bd(G)
    return [list(r) for r in R]