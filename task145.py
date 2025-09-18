def p(j):
	A=[K[:]for K in j];c,E=len(j),len(j[0]);k=set();W=[]
	for l in range(c):
		for J in range(E):
			if j[l][J]!=2 and(l,J)not in k:
				a,C=[],[(l,J)];k.add((l,J));e=0
				while C:
					K,w=C.pop();a.append((K,w))
					if j[K][w]==0:e+=1
					for(L,b)in[(0,1),(1,0),(0,-1),(-1,0)]:
						if 0<=K+L<c and 0<=w+b<E and j[K+L][w+b]!=2 and(K+L,w+b)not in k:k.add((K+L,w+b));C.append((K+L,w+b))
				W.append((e,a))
	d=max(K[0]for K in W);f=min(K[0]for K in W)
	for(e,a)in W:
		k=1 if e==d else 8 if e==f else 0
		if k:
			for(K,w)in a:
				if j[K][w]==0:A[K][w]=k
	return A

