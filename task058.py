def p(j):
	A=range;c=len(j);E=[[0]*c for W in A(c)];k,W=0,0;l=[(0,1),(1,0),(0,-1),(-1,0)]
	for J in A(c):
		E[k][W]=3
		if J<c-1:W+=1
	a=c-1;C=1
	while a>0:
		for e in A(2):
			if a>0:
				k,W=k+l[C][0],W+l[C][1]
				for J in A(a):
					E[k][W]=3
					if J<a-1:k,W=k+l[C][0],W+l[C][1]
				C=(C+1)%4
		a-=2
	return E

