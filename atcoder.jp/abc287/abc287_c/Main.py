N,M=map(int,input().split())
if N!=M+1:
  exit(print("No"))
D=dict(input().split() for i in range(M))
x,y=D.keys(),D.items()
while D:
  s,t=D.popitem()
  while t:
    t=D.pop(t,0)
    if t==s: exit(print('No'))
if x==t or x==s or y==t or y==s:
  print("No")
else:
  print('Yes')