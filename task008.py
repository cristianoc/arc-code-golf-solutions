def p(j,A=enumerate):
	c,E=[(c,b)for(c,E)in A(j)for(b,d)in A(E)if d==2],[(c,b)for(c,E)in A(j)for(b,d)in A(E)if d==8]
	if not c or not E:return j
	k=lambda W:(min(c for(c,E)in W),max(c for(c,E)in W),min(c for(E,c)in W),max(c for(E,c)in W));l,J,a,C=k(c);e,K,w,L=k(E);b=d=0
	if C<w:d=w-C-1
	elif L<a:d=L-a+1
	elif J<e:b=e-J-1
	elif K<l:b=K-l+1
	f,g={*c},{*E};return[[8 if(c,E)in g else 2 if(c-b,E-d)in f else 0 for(E,k)in A(j[0])]for(c,E)in A(j)]

