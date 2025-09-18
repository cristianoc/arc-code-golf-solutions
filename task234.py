def p(g):
 A=len(g);B=len(g[0])
 from collections import Counter
 C=Counter(v for r in g for v in r)
 bg=max(C,key=C.get)
 L={}
 for i,row in enumerate(g):
  for j,v in enumerate(row):
   if v!=bg:
    L.setdefault(v,set()).add((i,j))
 if not L: return g
 def bx(S):
  si=min(i for i,_ in S); ei=max(i for i,_ in S); sj=min(j for _,j in S); ej=max(j for _,j in S)
  return si,ei,sj,ej
 Rv=None; Rb=None
 for v,S in L.items():
  si,ei,sj,ej=bx(S)
  if (ei-si+1)*(ej-sj+1)==len(S):
   Rv=v; Rb=(si,ei,sj,ej); break
 if Rv is None or len(L)==1: return g
 Ov=next(v for v in L if v!=Rv); Os=L[Ov]
 M=set()
 for i,j in Os:
  ds=((i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1))
  if all(0<=x<A and 0<=y<B and g[x][y]==Ov for x,y in ds): M.add((i,j))
 if not M: return g
 msi,mei,msj,mej=bx(M)
 bsi,bei,bsj,bej=msi-1,mei+1,msj-1,mej+1
 h=[r[:] for r in g]
 for i,j in Os: h[i][j]=bg
 rsi,rei,rsj,rej=Rb
 def ov(a1,a2,b1,b2): return not (a2<b1 or a1>b2)
 vm=ov(bsj,bej,rsj,rej)
 di=dj=0
 bci=bsi+(bei-bsi+1)//2; bcj=bsj+(bej-bsj+1)//2
 rci=rsi+(rei-rsi+1)//2; rcj=rsj+(rej-rsj+1)//2
 if vm:
  di=1 if bci<rci else -1
 else:
  dj=1 if bcj<rcj else -1
 def adj(a,b):
  asi,aei,asj,aej=a; bsi,bei,bsj,bej=b
  vadj=ov(asj,aej,bsj,bej) and ((bsi-aei)==1 or (asi-bei)==1)
  hadj=ov(asi,aei,bsi,bei) and ((bsj-aej)==1 or (asj-bej)==1)
  return vadj or hadj
 oi=di; oj=dj; c=0
 while not adj((bsi,bei,bsj,bej),(rsi,rei,rsj,rej)) and c<42:
  c+=1; bsi+=di; bei+=di; bsj+=dj; bej+=dj; oi+=di; oj+=dj
 for i in range(max(0,bsi),min(A,bei+1)):
  for j in range(max(0,bsj),min(B,bej+1)):
   h[i][j]=Ov
 return h
