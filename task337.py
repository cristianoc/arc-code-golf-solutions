# ARC Task 337

def solve_d511f180(I):
    O = tuple(tuple(8 if v==5 else 5 if v==8 else v for v in r) for r in I)
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_d511f180(G)
    return [list(r) for r in R]
