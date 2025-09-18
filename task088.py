from collections import*
j=len
A=range
def p(c):
	E=[x for A in c for x in A];k=Counter(E).most_common();k=[C for C in k if C[1]==4][0][0];W,l=j(c),j(c[0]);J=[]
	for a in A(W):
		for C in A(l):
			if c[a][C]==k:J.append([a,C])
	e=min([i[1]for i in J]);K=max([i[1]for i in J]);w=min([i[0]for i in J]);L=max([i[0]for i in J]);c=c[w+1:L];c=[A[e+1:K]for A in c];W,l=j(c),j(c[0])
	for a in A(W):
		for C in A(l):
			if c[a][C]>0:c[a][C]=k
	return c

