def solve_9dfd6313(I):
    O=tuple(tuple(row) for row in zip(*I))
    return O
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_9dfd6313(G)
    return [list(r) for r in R]