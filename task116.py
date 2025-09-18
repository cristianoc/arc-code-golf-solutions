# ARC Task 116

def solve_4c4377d9(I):
    O = I[::-1]+I
    return O
def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_4c4377d9(G)
    return [list(r) for r in R]
