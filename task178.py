# ARC Task 178

def p(j):
    A = range
    c, E = len(j), len(j[0])
    k = []
    for W in A(c):
        if W==0 or j[W]!=j[W - 1]:k.append([j[W][0]])
    l = []
    J = -1
    for a in A(E):
        if a==0 or any(j[W][a]!=j[W][a - 1]for W in A(c)):l.append(j[0][a])
    if len(k)>1:return k
    else:return[l]
