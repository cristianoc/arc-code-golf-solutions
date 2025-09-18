# ARC Task 179

def solve_74dd1130(I):
    O = tuple(tuple(row) for row in zip(*I))
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_74dd1130(G)
    return [list(r) for r in R]
