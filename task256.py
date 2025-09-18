# ARC Task 256

def p(j, A = range):
    c = len(j)
    for E in A(c):
    if j[E][0]==2:
    k = 0
    while k<c and j[E][k]==2:k+=1
    for W in A(c):
    for l in A((k + E - W)*(W!=E)):j[W][l]=3 - 2*(W>E)
    return j
