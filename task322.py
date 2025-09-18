# ARC Task 322

def p(j, A = range):
    for c in A(len(j[0])):
    for E in A(len(j)):
    if j[E][c]:break
    else:continue
    for k in A(E, len(j)):j[k][c]=j[E][c]
    return j
