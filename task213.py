def Z(j,A):return len(set([J[A]for J in j]))
def p(c):
	E=enumerate;k,W=len(c),len(c[0]);l=Z(c,0)+Z(c,-1)<len(set(c[0]))+len(set(c[-1]));c=[[J if J!=5 else 0 for J in J]for J in c]
	for(J,a)in E(c):
		for(C,e)in E(a):
			if l:c[J][C]=max([c[0][C],c[-1][C]])
			else:c[J][C]=max([c[J][0],c[J][-1]])
	if l:c=[[J for J in J if J>0]for J in c];c=c[:len(c[0])]
	else:c=[J for J in c if sum(J)>0];c=[J[:len(c)]for J in c]
	return c

