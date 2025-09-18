def p(j):
	A=[k[:]for k in j];c,E=len(j),len(j[0])
	for k in range(c):
		for W in range(E):
			if j[k][W]==3:
				for(l,J)in[(0,1),(1,0),(0,-1),(-1,0)]:
					if 0<=k+l<c and 0<=W+J<E and j[k+l][W+J]==3:A[k][W]=8;break
	return A

