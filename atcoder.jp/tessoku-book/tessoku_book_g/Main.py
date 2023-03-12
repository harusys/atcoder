D = int(input())
N = int(input())
d = [0] * (D+2)
 
for _ in range(N):
  L, R = map(int, input().split())
  d[L] += 1
  d[R+1] -= 1

s = 0
for i in range(1,D+1):
  s += d[i]
  print(s)