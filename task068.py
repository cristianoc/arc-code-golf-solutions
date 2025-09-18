def p(j):
	A={};c=range
	for E in c(10):
		for k in c(10):
			if j[E][k]:A[j[E][k]]=A.get(j[E][k],0)+1
	W=next(A for(A,c)in A.items()if c==1);l,A=next((A,E)for A in c(10)for E in c(10)if j[A][E]==W);J=[[0]*10 for A in c(10)];J[l][A]=W
	for a in[-1,0,1]:
		for C in[-1,0,1]:
			if a or C:
				e,K=l+a,A+C
				if 0<=e<10 and 0<=K<10:J[e][K]=2
	return J

