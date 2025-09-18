# ARC Task 226

def f(j, A, c, E):
    if not(0<=A<len(j)and 0<=c<len(j[0])):return
    if j[A][c]:return
    j[A][c]=E
    for k, W in[(0, -1), (0, 1), (-1, 0), (1, 0)]:f(j, A + k, c + W, E)
def p(j):
    l, J = len(j), len(j[0])
    f(j, 0, 0, 1)
    for a in range(4):f(j, l//2 - 1 + a%2, J//2 - 1 + a//2, 2)
    f(j, l - 1, J - 1, 3)
    return j
