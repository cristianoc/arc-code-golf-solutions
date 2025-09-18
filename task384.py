# ARC Task 384

def p(j):A = [max(r)>0 for r in j].index(1)
c = len(j)-1-[max(r)>0for r in j][::-1].index(1)
p = [j for j, E in enumerate(zip(*j))if max(E)>0]
E = p[0]
k = p[-1]
return[[x for x in r[E:k + 1]for _ in[0]*2]for r in j[A:c + 1]for _ in[0]*2]
