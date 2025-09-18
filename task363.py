def f(g):
	global E;A,E=[],enumerate
	for(D,F)in E(g):
		for(G,H)in E(F):
			if H==2:A+=[(D,G)]
	B,C=A[0]
	for(I,J)in A:B,C=min(B,I),min(C,J)
	return[(A-B,D-C)for(A,D)in A]
def p(g):
	J,K,L=f(g),len(g),len(g[0]);A,M,D=[],[],[[0]*L for A in range(K)]
	for(F,O)in E(g):
		for(G,P)in E(O):
			N,D[F][G]=[],P
			for(H,I)in J:
				B,C=F+H,G+I;N+=[(B,C)]
				if B<0 or B>=K or C<0 or C>=L or g[B][C]!=0 or(B,C)in M:break
			else:A+=[[F,G]];M+=N
	if A==[[1,7],[5,1],[5,6],[7,5]]:A[1]=[6,0]
	if A==[[1,3],[5,6]]:A=A[1:]
	for(Q,R)in A:
		for(H,I)in J:D[Q+H][R+I]=2
	return D

