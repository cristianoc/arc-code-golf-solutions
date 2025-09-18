p=lambda j:list(map(list,zip(*[[0]*c.count(0)+[x for x in c if x]for c in zip(*j)])))

