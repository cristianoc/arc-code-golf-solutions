j=range
A=enumerate
def W(p,c,E,k):
	for W in j(c,c+k):
		for l in j(E,E+k):
			if W<len(p)and l<len(p[0]):
				if p[W][l]==0:return 0
	return 1
def l(p):
	J,a=len(p),len(p[0])
	for l in j(a-2,1,-1):
		for C in j(0,J-l):
			for A in j(0,a-l):
				if W(p,C,A,l):return C,A,l
	return-1
def N(p):
	W=0
	for l in p:
		for a in l:
			if a:W+=1
	return W
def b(p,e,K,w,k):
	W=0
	for l in j(e-k,e+w+k):
		for a in j(K-k,K+w+k):
			if p[l][a]:W+=1
	return W
def a(p):
	a,C,A=l(p);J=N(p);W=1
	while 1:
		if J==b(p,a,C,A,W):return A+2*W,a-W,C-W
		W+=1
def C(L):
	b,C=len(L),len(L[0]);W=[W[:]for W in L]
	for(l,J)in A(L):
		for(a,d)in A(J):
			if W[a][C-1-l]==0:W[a][C-1-l]=L[l][a]
	return W
def p(L):
	W,l,A=a(L);d=[[0]*W for l in j(W)]
	for J in j(l,l+W):
		for b in j(A,A+W):d[J-l][b-A]=L[J][b]
	d=C(C(C(d)));f=[W[:]for W in L]
	for J in j(l,l+W):
		for b in j(A,A+W):f[J][b]=d[J-l][b-A]
	return f

