# ARC Task 012

def p(j, A = range(-2, 3), c = enumerate, E = abs):k = [E[:]for E in j]
[k[I + D].__setitem__(C + F, H if E(D)==E(F)else B[C - 1])for(I, B)in c(j)for(C, H)in c(B)if H and B[C - 1]*B[C + 1]for D in A for F in A if E(D)==E(F)or not D * F]
return k
