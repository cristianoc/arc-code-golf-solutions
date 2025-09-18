# ARC Task 135

def solve_5bd6f4ac(I):
    O = tuple(tuple(r[6:9]) for r in I[:3])
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_5bd6f4ac(G)
    return [list(r) for r in R]
