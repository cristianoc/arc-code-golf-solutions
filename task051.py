# ARC Task 051

def p(j):
    A = range
    c = [l[:]for l in j]
    E, k = len(j), len(j[0])
    W = {}
    for l in A(E):
        for J in A(k):
        if j[l][J]:W[j[l][J]]=W.get(j[l][J], 0)+1
    l, J, a = next((l, J, j[l][J])for l in A(E)for J in A(k)if j[l][J]and W[j[l][J]]==1)
    for(C, e)in[(0, 1), (1, 0), (0, -1), (-1, 0)]:
        K, w = l + C, J + e
        if(K<0)|(K>=E)|(w<0)|(w>=k)|(j[K][w]==0):
        L = 1
        while(0<=l - L * C<E)&(0<=J - L * e<k):
        if j[l - L * C][J - L * e]==0:c[l - L * C][J - L * e]=a
        L+=1
    return c
