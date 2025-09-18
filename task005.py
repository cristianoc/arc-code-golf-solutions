def p(j):
    h,w=len(j),len(j[0])
    d=[(a,b)for a in(-4,0,4)for b in(-4,0,4)if a|b];R=range
    A=[w]*10;B=[h]*10;C=[-1]*10;D=[-1]*10
    for y in R(h):
        for x in R(w):
            c=j[y][x]
            if x<A[c]:A[c]=x
            if y<B[c]:B[c]=y
            if x>C[c]:C[c]=x
            if y>D[c]:D[c]=y
    for c in R(1,10):
        if C[c]-A[c]==2 and D[c]-B[c]==2:
            X,Y=A[c],B[c];break
    o=[[0]*w for _ in j]
    for r in R(3):o[Y+r][X:X+3]=j[Y+r][X:X+3]
    M=[(rx,ry)for ry in R(3)for rx in R(3)if j[Y+ry][X+rx]]
    for a,b in d:
        x=X+a;y=Y+b;c=0
        for ry in R(3):
            for rx in R(3):
                u,v=x+rx,y+ry
                if 0<=u<w and 0<=v<h and j[v][u]:
                    c=j[v][u];break
            if c:break
        if not c:continue
        x=X;y=Y
        while 1:
            x+=a;y+=b
            if not(-3<x<w and-3<y<h):break
            for rx,ry in M:
                u,v=x+rx,y+ry
                if 0<=u<w and 0<=v<h:o[v][u]=c
                
    return o
