N,M=map(int,input().split())
a=set([int(input()) for _ in range(M)])
dp=[0]*(N+1)
dp[0]=1
mod=10**9+7

for i in range(1,N+1):
  if i in a:
    continue
  dp[i]=(dp[i-1]+dp[i-2])%mod

print(dp[N])