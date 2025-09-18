def p(j,A=len,c=range):
	E='r';k='c';W,l,J=A(j),A(j[0]),{}
	for a in c(W):
		for C in c(l):
			e=j[a][C]
			if e in J:J[e][E]+=[a];J[e][k]+=[C]
			else:J[e]={E:[a],k:[C]}
	K=sorted([[A(J[e][E])*(max(J[e][k])-min(J[e][k])),e]for e in J if e>0])[0][1];j=[[K if J==K else 0 for J in J]for J in j];J=J[K];j=[E[min(J[k]):max(J[k])+1]for E in j];j=j[min(J[E]):max(J[E])+1];return j

