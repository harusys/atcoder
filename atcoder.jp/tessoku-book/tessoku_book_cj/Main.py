import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

for _ in range(Q):
  idx = bisect.bisect_left(A, int(input()))
  print(idx)