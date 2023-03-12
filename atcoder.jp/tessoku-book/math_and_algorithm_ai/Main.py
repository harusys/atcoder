N,Q = map(int, input().split())
A = list(map(int, input().split()))

S = [ None ] * (N + 1)
S[0] = 0
for i in range(N):
  S[i+1] = S[i] + A[i]

for j in range(Q):
  L, R = map(int, input().split())
  print(S[R] - S[L-1])