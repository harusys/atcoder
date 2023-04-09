_,D,*T=map(int,open(0).read().split())
for p,t in zip(T,T[1:]):
  if t-p<=D: exit(print(t))
print(-1)