from collections import*
def p(j):
 A=[x for k in j for x in k];c=Counter(A).most_common(3);c=[c for c in c if c[0]>0][-1][0];j=[k for k in j if c in k];E=[]
 for k in j:
  for W in range(len(k)):
   if k[W]==c:E+=[W]
 return[k[min(E):max(E)+1]for k in j]

