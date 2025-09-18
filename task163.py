# ARC Task 163

def p(g):
    R = range
    for r in R(3):
    for c in R(3):
    b = [[g[4 * r + i][4 * c + j]for j in R(3)]for i in R(3)]
    for i in R(3):
    for j in R(3):
    if b[i][j]==4:
    z = [[0]*11for _ in R(11)]
    for x in R(3):
    for y in R(3):z[4 * i + x][4 * j + y]=b[x][y]
    for k in R(11):z[k][3]=z[k][7]=z[3][k]=z[7][k]=5
    return z
