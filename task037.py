def p(j,A=range):
	c,E=len(j),len(j[0]);k,W={},[A[:]for A in j]
	for l in A(c):
		for J in A(E):
			a=j[l][J]
			if a:k.setdefault(a,[]).append((l,J))
	for a in k:
		(C,e),(K,w)=k[a];L=1 if K>C else-1;b=1 if w>e else-1
		for d in A(abs(K-C)+1):W[C+d*L][e+d*b]=a
	return W

