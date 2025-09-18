# ARC Task 150

def solve_67a3c6ac(I):
    O = tuple(tuple(reversed(r)) for r in I)
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_67a3c6ac(G)
    return [list(r) for r in R]
