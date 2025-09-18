def p(j,A=range):
	c,E=len(j),len(j[0]);k=[0 for W in A(E)]
	for W in A(E):
		for l in A(c):
			if j[l][W]>0:k[W]+=1
			j[l][W]=0
	J=min([W for W in k if W>0]);W=k.index(J)
	for l in A(k[W]):j[-(l+1)][W]=2
	W=k.index(max(k))
	for l in A(k[W]):j[-(l+1)][W]=1
	return j

