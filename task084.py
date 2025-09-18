# ARC Task 084

def p(j):
    A = len(j)
    for c in range(1, len(j[0])):j[A - 1][c]=4
    j[A - c-1][c]=2
    return j
