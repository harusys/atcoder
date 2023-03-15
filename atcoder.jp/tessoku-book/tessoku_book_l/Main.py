N,K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
  sum = 0
  for a in A:
    sum += x // a
  return sum >= K

L = 1
R = 10 ** 9
while L < R:
  M = (L+R) // 2

  if check(M):
    R = M
  else:
    L = M + 1

print(L)