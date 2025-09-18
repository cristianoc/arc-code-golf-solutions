def solve_6fa7a44f(I):
    O=I+I[::-1]
    return O
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_6fa7a44f(G)
    return [list(r) for r in R]