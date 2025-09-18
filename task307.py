# ARC Task 307

def solve_c59eb873(I):
    O = tuple(tuple(v for v in r for _ in range(2)) for r in I for _ in range(2))
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_c59eb873(G)
    return [list(r) for r in R]
