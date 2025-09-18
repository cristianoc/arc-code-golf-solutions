# ARC Task 151

def p(j):A = lambda c:list(map(all, c)).index(1)
E, k = A(j), A(zip(*j))
j[E - 1][k - 1:k + 2]=j[E + 1][k - 1:k + 2]=[4]*3
j[E][k - 1]=j[E][k + 1]=4
return j
