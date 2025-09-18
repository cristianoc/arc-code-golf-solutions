# ARC Task 087

def solve_3c9b0459(I):
    O = tuple(tuple(reversed(r)) for r in I[::-1])
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_3c9b0459(G)
    return [list(r) for r in R]
