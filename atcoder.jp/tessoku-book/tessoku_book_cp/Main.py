N = int(input())
h = list(map(int, input().split()))

dp = [ None ] * (N)
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
  dp[i] = min(dp[i-1] + abs(h[i-1]-h[i]), dp[i-2] + abs(h[i-2]-h[i]))

P = []
p = N
while True:
  P.append(p)
  if p == 1:
    break
  if dp[p-2] + abs(h[p-2]-h[p-1]) == dp[p-1]:
    p = p - 1
  else:
    p = p - 2
P.reverse()

print(len(P))
print(" ".join([str(p) for p in P]))