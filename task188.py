p = lambda j, A = len:[r[:A(r)//2]for r in j]if A(j[0])%2<1and all(r[:A(r)//2]==r[A(r)//2:]for r in j)else j[:A(j)//2]
