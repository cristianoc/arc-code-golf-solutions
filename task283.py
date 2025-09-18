# ARC Task 283

def f(j, p, A, c, E, k):
    for W in range(A, E + 1):
    for l in range(p, c + 1):j[W][l]=k
def z(j, p, A, c, E):f(j, p, A, c, E, 4)
f(j, p + 1, A + 1, c - 1, E - 1, 2)
j[A][p]=j[A][c]=j[E][p]=j[E][c]=1
def p(j):
    J, a = len(j), len(j[0])
    for C in range(J * a):
    l, W = C%a, C//a
    if j[W][l]==5:
    c, E = l, W
    while c<a - 1and j[E][c + 1]==5:c+=1
    while E<J - 1and j[E + 1][c]==5:E+=1
    z(j, l, W, c, E)
    return j
