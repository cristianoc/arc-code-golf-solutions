# ARC Task 380

def solve_ed36ccf7(I):
    O = tuple(tuple(row) for row in zip(*I))[::-1]
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_ed36ccf7(G)
    return [list(r) for r in R]
