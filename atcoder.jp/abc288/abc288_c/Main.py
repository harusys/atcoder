N,M=map(int,input().split())
p=[-1]*(N+1)
cnt=0

def root(x):
  if p[x] < 0:
    return x
  p[x] = root(p[x])
  return p[x]

def unite(x, y):
  x = root(x)
  y = root(y)
  if x == y:
    return
  p[y] = x

for _ in range(M):
  x,y=map(int, input().split())
  if root(x)==root(y):
    cnt+=1
  unite(x,y)

print(cnt)