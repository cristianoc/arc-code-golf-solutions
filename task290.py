def p(j):
	j=[c for c in j if sum(c)>0];A=[];c=[]
	for E in j:
		for k in range(len(E)):
			if E[k]>0:A.append(k);c.append(E[k])
	c=list(set(c));c={c[0]:c[1],c[1]:c[0]};j=[c[min(A):max(A)+1]for c in j];j=[[c[A]for A in A]for A in j];return j

