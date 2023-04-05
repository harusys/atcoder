N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
  dp[i] = min(dp[i-1] + A[i-2], dp[i-2] + B[i-3])

P = []
p = N
while True:
  P.append(p)
  if p == 1:
    break
  if dp[p-1] + A[p-2] == dp[p]:
    p = p - 1
  else:
    p = p - 2
P.reverse()

print(len(P))
print(" ".join([str(p) for p in P]))