# ARC Task 055

def p(j, A = range):
    c, E = len(j), len(j[0])
    k = [A[:]for A in j]
    W, l = [A for A in A(c)if all(A==8 for A in j[A])]
    J, a = [C for C in A(E)if all(j[A][C]==8 for A in A(c))]
    for C in A(c):
        for e in A(E):
        if not k[C][e]:
        if C<W and J<e<a:k[C][e]=2
        elif W<C<l and e<J:k[C][e]=4
        elif W<C<l and J<e<a:k[C][e]=6
        elif W<C<l and e>a:k[C][e]=3
        elif C>l and J<e<a:k[C][e]=1
    return k
