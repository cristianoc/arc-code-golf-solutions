def p(j):
	for A in range(1,len(j)-1):
		for c in range(1,len(j[0])-1):
			if j[A][c]==8:
				E=[]
				for k in[-1,0,1]:
					for W in[-1,0,1]:
						if(k or j)and j[A+k][c+W]:E.append(j[A+k][c+W])
				l=max(set(E),key=E.count);J=[[j[A+E][c+k]for k in[-1,0,1]]for E in[-1,0,1]];J[1][1]=l;return J

