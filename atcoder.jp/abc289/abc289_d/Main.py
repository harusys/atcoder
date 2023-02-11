_=input()
a=set(map(int, input().split()))
_=input()
b=set(map(int, input().split()))
x=int(input())
dp=[False]*(x+1)
dp[0]=True
for i in range(x+1):
  if i in b: continue
  for aa in a:
    if i<aa: continue
    dp[i]|=dp[i-aa]
print('Yes' if dp[x] else 'No')