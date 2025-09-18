def p(j):
	A=range;c=len;E=[W[:]for W in j];k=set()
	for W in A(c(j)):
		for l in A(c(j[0])):
			if j[W][l]and(W,l)not in k:
				J,a=[(W,l)],[(W,l)];k.add((W,l));C=j[W][l]
				while a:
					e,K=a.pop()
					for(w,L)in[(0,1),(1,0),(0,-1),(-1,0)]:
						b,d=e+w,K+L
						if 0<=b<c(j)and 0<=d<c(j[0])and j[b][d]==C and(b,d)not in k:k.add((b,d));J.append((b,d));a.append((b,d))
				f=min(W[0]for W in J);g=max(W[0]for W in J);h=min(W[1]for W in J);i=max(W[1]for W in J)
				for e in A(f+1,g):
					for K in A(h+1,i):E[e][K]=8
	return E

