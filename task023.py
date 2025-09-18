def p(g):
    h,w=len(g),len(g[0]);Z=5;r=2;b=8
    S={(i,j) for i in range(h) for j in range(w) if g[i][j]==Z}
    V=[];H=[];Q=[]
    for i in range(h-2):
        for j in range(w):
            t=((i,j),(i+1,j),(i+2,j))
            if all(c in S for c in t):V.append(t)
    for i in range(h):
        for j in range(w-2):
            t=((i,j),(i,j+1),(i,j+2))
            if all(c in S for c in t):H.append(t)
    for i in range(h-1):
        for j in range(w-1):
            t=((i,j),(i,j+1),(i+1,j),(i+1,j+1))
            if all(c in S for c in t):Q.append(t)
    L=sorted(S);I={c:i for i,c in enumerate(L)}
    def M(t):
        m=0
        for c in t:m|=1<<I[c]
        return m
    A=[(0,s,M(s)) for s in V]+[(1,s,M(s)) for s in H]+[(2,s,M(s)) for s in Q]
    D={}
    for a in A:
        for c in a[1]:D.setdefault(c,[]).append(a)
    for c in D:D[c].sort(key=lambda x:(x[0],x[1][0]))
    F=(1<<len(L))-1
    def dfs(m):
        if m==F:return []
        for i,c in enumerate(L):
            if m>>i&1==0:break
        for t,s,mm in D.get(c,()):
            if mm&m==0:
                r=dfs(m|mm)
                if r is not None:return [(t,s)]+r
    P=dfs(0)
    x=[r[:] for r in g]
    for t,s in P:
        col=r if t<2 else b
        for i,j in s:x[i][j]=col
    return x
