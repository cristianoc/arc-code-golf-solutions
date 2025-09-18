# ARC Task 249

def solve_a416b8f3(I):
    O = tuple(tuple(a + b) for a, b in zip(I, I))
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_a416b8f3(G)
    return [list(r) for r in R]
