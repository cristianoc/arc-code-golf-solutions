# ARC Task 013

def p(j, A = range):
    c, E = len(j), len(j[0])
    p = [(l, L, j[l][L])for l in A(c)for L in A(E)if j[l][L]]
    p.sort()
    if len(p)==2:
    k, W = p
    if k[0]==W[0]:
    l, J, a = k
    C, e = W[1], W[2]
    K = abs(C - J)
    for w in A(c):j[w][J]=a
    j[w][C]=e
    if K:
    L = max(J, C)+K
    b = 0
    d = [a, e]
    if C<J:d = d[::-1]
    while L<E:
    for w in A(c):j[w][L]=d[b%2]
    L+=K
    b+=1
    elif k[1]==W[1]:
    L, f, a = k[1], k[0], k[2]
    g, e = W[0], W[2]
    K = abs(g - f)
    for w in A(E):j[f][w]=a
    j[g][w]=e
    if K:
    l = g + K
    b = 0
    d = [a, e]
    while l<c:
    for w in A(E):j[l][w]=d[b%2]
    l+=K
    b+=1
    elif k[0]==0and W[0]==c - 1:
    f, J, a = k
    g, C, e = W
    K = abs(C - J)
    for w in A(c):j[w][J]=a
    j[w][C]=e
    if K:
    L = C + K
    b = 0
    d = [a, e]
    while L<E:
    for w in A(c):j[w][L]=d[b%2]
    L+=K
    b+=1
    elif(k[1]==0and W[1]==E - 1)or(W[1]==0and k[1]==E - 1):
    if k[1]==0:f, J, a = k
    g, C, e = W
    else:f, J, a = W
    g, C, e = k
    K = abs(g - f)
    for w in A(E):j[f][w]=a
    j[g][w]=e
    if K:
    l = max(f, g)+K
    b = 0
    d = [a, e]
    if g<f:d = d[::-1]
    while l<c:
    for w in A(E):j[l][w]=d[b%2]
    l+=K
    b+=1
    return j
