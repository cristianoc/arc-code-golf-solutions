# ARC Task 047

def p(j):
    A = range
    c = [[0]*9 for c in A(9)]
    E = [(c, E, j[c][E])for c in A(9)for E in A(9)if j[c][E]]
    for(k, W, l)in E:
        for J in range(9):c[k][J]=c[J][W]=l
    c[E[0][0]][E[1][1]]=c[E[1][0]][E[0][1]]=2
    return c
