def p(j):
	A=range;c,E=len(j),len(j[0]);k=[k for k in A(c)if all(j[k][A]==0 for A in A(E))];W=[k for k in A(E)if all(j[A][k]==0 for A in A(c))];k=[-1]+k+[c];W=[-1]+W+[E];l=[]
	for J in A(len(k)-1):
		a=[]
		for C in A(len(W)-1):
			for e in A(k[J]+1,k[J+1]):
				for K in A(W[C]+1,W[C+1]):
					if j[e][K]:a.append(j[e][K]);break
				else:continue
				break
		if a:l.append(a)
	return l

