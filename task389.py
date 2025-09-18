# ARC Task 389

def p(j):A = [i for s in j for i in s]
A = [c for c in set(A)if c not in[0, 5]][0]
j = [[A if C==5 else 0 for C in R]for R in j]
return j
