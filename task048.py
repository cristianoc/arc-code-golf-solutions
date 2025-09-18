# ARC Task 048

def f(j, A, c):
    global W
    l.append((j, A))
    for E in C(j - 1, j + 2):
        for k in C(A - 1, A + 2):
        if(E, k)in l:continue
        l.append((E, k))
        if E<0 or E>=J or k<0 or k>=a or(E, k)in[(K, L), (K + 1, L), (K, L + 1), (K + 1, L + 1)]:continue
        if c[E][k]==2:W = 8
        if c[E][k]==8:f(E, k, c)
def p(c):
    global W, l, K, L, J, a, C
    W, l, J, a, C, e = 0, [], len(c), len(c[0]), range, enumerate
    for(K, w)in e(c):
        for(L, b)in e(w):
        if b==2:
        for E in C(K - 1, K + 3):
        for k in C(L - 1, L + 3):
        if E>=0 and E<J and k>=0 and k<a and c[E][k]==8:f(E, k, c)
        return[[W]]
