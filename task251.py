# ARC Task 251

def p(j, A = range):
    c, E = len(j), len(j[0])
    k = [[0]*E for c in A(c)]
    W = []
    for l in A(c):
        for J in A(E):
        if l * J==0 or l==c - 1 or J==E - 1:
    if j[l][J]==0:k[l][J]=1
    W.append((l, J))
    while W:
        a, C = W.pop(0)
        for(e, K)in[(-1, 0), (1, 0), (0, -1), (0, 1)]:
        w, L = a + e, C + K
    if 0<=w<c and 0<=L<E and j[w][L]==0 and not k[w][L]:k[w][L]=1
    W.append((w, L))
    b = [[j[c][E]if j[c][E]!=0 or k[c][E]else 1 for E in A(E)]for c in A(c)]
    return b
