p=lambda j:[[k]for k,_ in __import__('collections').Counter(i for r in j for i in r).most_common(5)[2:]]

