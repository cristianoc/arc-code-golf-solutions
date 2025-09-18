# ARC Task 303

def p(j, A = range):
    c, E = len(j), len(j[0])
    for k in A(c):
    if sum(j[k])==0:j[k]=[2]*E
    for W in A(E):
    if all(j[k][W]in[0, 2]for k in A(c)):
    for k in A(c):j[k][W]=2
    return j
