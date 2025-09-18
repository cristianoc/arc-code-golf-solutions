def p(j,A=len,c=enumerate,E=min,k=max,W=range):
	l,J=A(j),A(j[0]);a=[(L,b)for(L,f)in c(j)for(b,K)in c(f)if K==5];C=E(L for(L,f)in a);e=k(L for(L,f)in a);K=E(L for(f,L)in a);w=k(L for(f,L)in a)
	for L in range(C+1,e):j[L][K+1:w]=[8]*(w-K-1)
	b=None;d=0,0
	for f in W(K,w+1):
		if j[C][f]==0:b=C,f;d=-1,0;break
	if not b:
		for f in range(K,w+1):
			if j[e][f]==0:b=e,f;d=1,0;break
	if not b:
		for L in range(C,e+1):
			if j[L][K]==0:b=L,K;d=0,-1;break
	if not b:
		for L in range(C,e+1):
			if j[L][w]==0:b=L,w;d=0,1;break
	L,f=b;g,h=d
	while 0<=L<l and 0<=f<J and j[L][f]==0:j[L][f]=8;L+=g;f+=h
	return j

