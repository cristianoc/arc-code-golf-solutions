p = lambda j:(A:=len(set(sum(j, []))-{0}), [[x for x in r for _ in range(A)]for r in j for _ in range(A)])[1]
