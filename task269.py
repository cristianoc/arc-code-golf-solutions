p=lambda j:(A:=sum(c>0for r in j for c in r),[sum(([x]*A for x in r),[])for r in j for _ in range(A)])[1]

