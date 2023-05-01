N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
  q = list(map(int, input().split()))
  i = q[0]
  k = q[1]
  if i == 1:
    A[k-1] = q[2]
  if i == 2:
    print(A[k-1])