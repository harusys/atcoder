N,X = map(int, input().split())
A = list(map(int, input().split()))

def search(x, a):
  L = 0
  R = N-1
  while L <= R:
    M = (L+R) // 2
    if x < a[M]:
      R = M-1
    if x == a[M]:
      return M
    if x > a[M]:
      L = M+1
  return -1

Answer = search(X, A)
print(Answer + 1)