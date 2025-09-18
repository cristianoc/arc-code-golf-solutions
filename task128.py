# ARC Task 128

def p(j):
    A = [[0]*len(j[0])for a in j]
    c = set()
    for E in range(len(j)):
        for k in range(len(j[0])):
        if j[E][k]and(E, k)not in c:
    W, l = [(E, k)], [(E, k)]
    c.add((E, k))
    J = j[E][k]
        while l:
        a, C = l.pop()
        for(e, K)in[(0, 1), (1, 0), (0, -1), (-1, 0)]:
    if 0<=a + e<len(j)and 0<=C + K<len(j[0])and j[a + e][C + K]==J and(a + e, C + K)not in c:c.add((a + e, C + K))
    W.append((a + e, C + K))
    l.append((a + e, C + K))
        w = max(a for(a, C)in W)-min(a for(a, C)in W)+1
        for(a, C)in W:A[a - w][C]=J
    return A
