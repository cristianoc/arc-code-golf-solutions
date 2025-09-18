from collections import Counter, deque

def p(g):
    h,w=len(g),len(g[0])
    # Least frequent color in the whole grid
    cnt=Counter(v for r in g for v in r)
    least=min(cnt, key=cnt.get)
    # Background as most frequent; dominant foreground = most common excluding bg
    bg=max(cnt, key=cnt.get)
    dom=max((c for c in cnt if c!=bg), key=cnt.get, default=bg)
    # Horizontal mirror across vertical axis: compare with vmirror
    g2=[[g[i][w-1-j] for j in range(w)] for i in range(h)]
    g1=[[g[i][j] if g[i][j]==g2[i][j] else least for j in range(w)] for i in range(h)]
    # Vertical mirror across horizontal axis
    g3=g1[::-1]
    g4=[[g1[i][j] if g1[i][j]==g3[i][j] else least for j in range(w)] for i in range(h)]
    # Compress: drop rows/cols that are uniform
    keep_rows=[i for i in range(h) if len(set(g4[i]))>1]
    if not keep_rows:
        keep_rows=list(range(h))
    cols=list(zip(*g4))
    keep_cols=[j for j in range(w) if len(set(cols[j]))>1]
    if not keep_cols:
        keep_cols=list(range(w))
    out=[[g4[i][j] for j in keep_cols] for i in keep_rows]
    # Replace least with dominant foreground color
    for i in range(len(out)):
        for j in range(len(out[0])):
            if out[i][j]==least:
                out[i][j]=dom
    return out
