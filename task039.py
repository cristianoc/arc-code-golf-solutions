j=len
A=range
def p(c):
	E,k=j(c),j(c[0]);W=[]
	for l in A(E):
		for J in A(k):
			if c[l][J]>0:W.append([l,J])
	a=min([W[1]for W in W]);C=max([W[1]for W in W]);e=min([W[0]for W in W]);K=max([W[0]for W in W]);C=C-(C-a)//2;K=K-(K-e)//2;c=c[e:K];c=[W[a:C]for W in c];return c

