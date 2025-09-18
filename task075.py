def p(j):
	A=range;c=[A[:]for A in j];E=[[j[k][A]for A in A(3)]for k in A(3)]
	for k in A(9):
		for W in A(4,13):
			if j[k][W]==1:
				for l in A(-1,2):
					for J in A(-1,2):
						if 0<=k+l<9and 4<=W+J<13:c[k+l][W+J]=E[l+1][J+1]
	return c

