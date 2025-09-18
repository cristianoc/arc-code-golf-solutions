# ARC Task 321

def p(j):
    for A in range(4):
    for c in range(4):
    if j[A][c + 5]>0:j[A][c + 10]=j[A][c + 5]
    if j[A][c]>0:j[A][c + 10]=j[A][c]
    return[R[10:]for R in j]
