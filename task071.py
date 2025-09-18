def p(g):
 from collections import defaultdict
 def rect(c):
  if not c:return False
  rs,cs=zip(*c)
  return len(c)==(max(rs)-min(rs)+1)*(max(cs)-min(cs)+1)
 H,W=len(g),len(g[0])
 C=defaultdict(list)
 for r in range(H):
  for c in range(W):
   if g[r][c]:C[g[r][c]].append((r,c))
 if not C:return[[0]*W for _ in range(H)]
 blue=max([k for k,v in C.items() if rect(v)],key=lambda k:len(C[k]),default=None)
 red=max([k for k in C if k!=blue and not rect(C[k])]or[k for k in C if k!=blue],key=lambda k:len(C[k]))
 S,Sset=C[red],set(C[red])
 Bset=set(C[blue])if blue else set()
 t=max(range(2*W-1),key=lambda t:sum(1 for r,c in S if 0<=(m:=t-c)<W and((r,m)in Sset or(r,m)in Bset)),default=min(c for r,c in S)+max(c for r,c in S))
 out=[[0]*W for _ in range(H)]
 for r,c in S:out[r][c]=red
 if blue:
  for r,c in C[blue]:
   if 0<=(o:=t-c)<W and(r,o)in Sset:out[r][c]=red
 return out
