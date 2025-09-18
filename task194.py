j=lambda A:[[*i]for i in zip(*A[::-1])]
p=lambda c:[a+b for a,b in zip(c,j(c))]+[a+b for a,b in zip(j(j(j(c))),j(j(c)))]

