H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
ans = 0
def f(x, y, t):
  global ans
  if x >= W or y >= H:
    return
  if not A[y][x] in t:
    if x == W-1 and y == H-1:
      ans += 1
      return
    t.add(A[y][x])
    f(x+1, y, t)
    f(x, y+1, t)
    t.remove(A[y][x])
  return
f(0, 0, set())
print(ans)