def p(j,A=range):
	c=[J[:]for J in j]
	for E in A(1,10):
		k=[(J,k)for J in A(len(j))for k in A(len(j[0]))if j[J][k]==E]
		for W in A(len(k)):
			for l in A(W+1,len(k)):
				J,a=k[W];C,e=k[l]
				if J==C:
					for K in A(min(a,e),max(a,e)+1):c[J][K]=8
				elif a==e:
					for w in A(min(J,C),max(J,C)+1):c[w][a]=8
		for(J,C)in k:c[J][C]=1
	return c

