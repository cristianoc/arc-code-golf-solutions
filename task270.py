def p(M):
 R,C=len(M),len(M[0]);O=[[0]*C for _ in range(R)];P={}
 for r in range(R):
  for c in range(C):
   v=M[r][c]
   if v in(1,2):P[v]=(r,c);O[r][c]=v
 T={3:P[2],7:P[1]}
 for r in range(R):
  for c in range(C):
   v=M[r][c]
   if v not in(0,1,2):
    tr,tc=T[v]
    if r==tr:
     nc=tc+(1 if c>tc else-1)
     (O[r].__setitem__(nc,v) if 0<=nc<C and not O[r][nc] else O[r].__setitem__(c,v))
    elif c==tc:
     nr=tr+(1 if r>tr else-1)
     (O[nr].__setitem__(c,v) if 0<=nr<R and not O[nr][c] else O[r].__setitem__(c,v))
    else:
     b,d=None,1e9
     for ar,ac in((tr,tc+1),(tr,tc-1),(tr+1,tc),(tr-1,tc)):
      if 0<=ar<R and 0<=ac<C and not O[ar][ac]and(ar==r or ac==c):
       dist=abs(r-ar)+abs(c-ac)
       if dist<d:d,b=dist,(ar,ac)
     (O[b[0]].__setitem__(b[1],v) if b else O[r].__setitem__(c,v))
 return O

