N,K=map(int,input().split())
S=input()
ans=''
cnt=0
for s in S:
  if s == 'o' and cnt < K:
    ans += 'o'
    cnt += 1
  else:
    ans += 'x'
print(ans)