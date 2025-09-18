from collections import*
def p(m,K=enumerate):
	a=[(i,j)for(i,r)in K(m)for(j,v)in K(r)if v]
	if not a:return[]
	v=Counter(m[i][j]for(i,j)in a).most_common(1)[0][0];x=[(i,j)for(i,j)in a if m[i][j]==v];h,b=min(i for(i,_)in x),min(j for(_,j)in x);c,g=max(i for(i,_)in x)+1,max(j for(_,j)in x)+1;return[m[i][b:g]for i in range(h,c)]

