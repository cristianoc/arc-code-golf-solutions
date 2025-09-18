from collections import Counter
def mostcolor(g):
 if not g or not g[0]:return 0
 c=Counter(v for r in g for v in r)
 m=max(c.values())
 s=[k for k,v in c.items() if v==m]
 return 0 if 0 in s else min(s)


def objects(g,univalued=False,diagonal=False,without_bg=True):
 if not g or not g[0]:return[]
 H,W=len(g),len(g[0])
 bg=mostcolor(g)if without_bg else None
 s=[[False]*W for _ in range(H)]
 c=[]
 n=[(1,0),(-1,0),(0,1),(0,-1)]+[(1,1),(1,-1),(-1,1),(-1,-1)]*diagonal
 for i in range(H):
  for j in range(W):
   v=g[i][j]
   if s[i][j]or(without_bg and v==bg):continue
   t=v if univalued else None
   q=[(i,j)];s[i][j]=True;cells=[]
   while q:
    x,y=q.pop();v=g[x][y]
    if(univalued and v!=t)or(not univalued and without_bg and v==bg):continue
    cells.append((v,(x,y)))
    for dx,dy in n:
     nx,ny=x+dx,y+dy
     if 0<=nx<H and 0<=ny<W and not s[nx][ny]:
      if univalued:
       if g[nx][ny]==t:s[nx][ny]=True;q.append((nx,ny))
      else:
       if not(without_bg and g[nx][ny]==bg):s[nx][ny]=True;q.append((nx,ny))
   if cells:c.append(cells)
 return c


def bbox(o):
 it=iter(o)
 _,(i0,j0)=next(it)
 mi=ma=i0;mj=mj2=j0
 for _,(i,j) in it:
  if i<mi:mi=i
  elif i>ma:ma=i
  if j<mj:mj=j
  elif j>mj2:mj2=j
 return mi,mj,ma,mj2


def normalize(o):
 if not o:return o
 mi,mj,_,_=bbox(o)
 return[(v,(i-mi,j-mj))for v,(i,j)in o]
def shift(o,d):
 di,dj=d
 return[(v,(i+di,j+dj))for v,(i,j)in o]
def vmirror(o):
 if not o:return o
 _,mj,_,mj2=bbox(o)
 return[(v,(i,mj+mj2-j))for v,(i,j)in o]
def hmirror(o):
 if not o:return o
 mi,_,mi2,_=bbox(o)
 return[(v,(mi+mi2-i,j))for v,(i,j)in o]
def dmirror(o):
 if not o:return o
 mi,mj,_,_=bbox(o)
 return[(v,(j-mj+mi,i-mi+mj))for v,(i,j)in o]
def cmirror(o):
 return vmirror(dmirror(vmirror(o)))


def paint(g,o):
 if not g or not g[0]:return g
 H,W=len(g),len(g[0])
 out=[list(r)for r in g]
 for v,(i,j)in o:
  if 0<=i<H and 0<=j<W:out[i][j]=v
 return out
def occurrences(g,o):
 if not g or not g[0]:return set()
 H,W=len(g),len(g[0])
 n=normalize(o)
 if not n:return set()
 mi,mj,ma,mj2=bbox(n)
 hi=ma-mi+1;hj=mj2-mj+1
 s=set()
 for si in range(H-hi+1):
  for sj in range(W-hj+1):
   if all(g[i][j]==v for v,(i,j)in shift(n,(si,sj))):s.add((si,sj))
 return s


def solve_36d67576(I):
 if not I or not I[0]:return I
 o=objects(I,univalued=False,diagonal=True,without_bg=True)
 if not o:return I
 obj=max(o,key=lambda o:len({v for v,_ in o}))
 t=[cmirror,dmirror,hmirror,vmirror]
 at=t+[lambda x,a=a,b=b:a(b(x))for a in t for b in t]
 p=[]
 for tf in at:
  tr=tf(obj);nt=normalize(tr)
  s=[(v,(i,j))for v,(i,j)in nt if v in{2,4}]
  if not s:continue
  bi=min(i for _,(i,_)in s);bj=min(j for _,(_,j)in s)
  for oi,oj in occurrences(I,s):
   p.append(shift(nt,(oi-bi,oj-bj)))
 return paint(I,{c for part in p for c in part})


# Keep the alias expected by your harness
p = solve_36d67576
