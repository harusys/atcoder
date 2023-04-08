N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
dp[0][0] = True

for i in range(1, S+1):
  dp[0][i] = False

for i in range(1, N+1):
  for j in range(S+1):
    # カードを選ばない場合
    dp[i][j] = dp[i-1][j]
    # カードを選ぶ場合
    if j - A[i-1] >= 0:
      if dp[i-1][j-A[i-1]]:
        dp[i][j] = True

if dp[N][S] == False:
  print("-1")
  exit()

P = []
p = S
for i in reversed(range(1,N+1)):
  if dp[i-1][p] == True:
    p = p - 0
  else:
    p = p - A[i-1]
    P.append(i)
P.reverse()

print(len(P))
print(" ".join([str(p) for p in P]))