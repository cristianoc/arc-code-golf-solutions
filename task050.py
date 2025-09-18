# ARC Task 050

def p(j):
	A=range;c=[e[:]for e in j];E,k=len(j),len(j[0]);W=[(e,l)for e in A(E)for l in A(k)if j[e][l]==8]
	for(l,J)in W:
		for(a,C)in[(0,1),(1,0),(0,-1),(-1,0)]:
			e=1
			while 0<=l+e*a<E and 0<=J+e*C<k:
				if j[l+e*a][J+e*C]==8:
					for K in A(1,e):c[l+K*a][J+K*C]=3
					break
				e+=1
	return c

