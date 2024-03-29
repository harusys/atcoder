N, W = map(int, input().split())
dp = [ [0] * (W+1) for _ in range(N+1) ]

for i in range(1, N+1):
  w, v = list(map(int, input().split()))
  for j in range(1,W+1):
    if j < w:
      dp[i][j] = dp[i-1][j]
    if j >= w:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[-1][-1])