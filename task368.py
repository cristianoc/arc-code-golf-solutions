def p(j,A=range):
	c=len(j);E=1;k,W=0,0;l=[0,5];J,a=0,0
	for C in A(c):
		for e in A(c):
			if j[C][e]not in l and E:
				E=0;J,a=C,e;K=C;w=e
				while K<c and j[K][e]not in l:K+=1
				while w<c and j[C][w]not in l:w+=1
				k=K-C;W=w-e
	for C in A(c-k+1):
		for e in A(c-W+1):
			if j[C][e]==5:
				for L in A(k):
					for b in A(W):j[C+L][e+b]=j[J+L][a+b]
	return j

