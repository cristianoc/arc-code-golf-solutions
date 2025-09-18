def p(j):
	A=range;c=set();E=[c[:]for c in j]
	def F(k,W):
		if(k,W)in c or not(0<=k<10 and 0<=W<10)or j[k][W]:return[]
		c.add((k,W));return[(k,W)]+sum([F(k+c,W+l)for(c,l)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
	for l in A(10):
		for J in A(10):
			if j[l][J]==0 and(l,J)not in c:
				a=F(l,J)
				for(C,e)in a:E[C][e]=abs(len(a)-4)
	return E

