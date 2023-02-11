N,M=map(int,input().split())
if M==0:
  print(" ".join(map(str, [i for i in range(1,N+1)])))
  exit()

L=list(map(int, input().split()))
ans=[]
match=[]
for i in range(1,N+1):
  if i in L:
    match.append(i)
  else:
    if len(match)!=0:
      match.append(i)
      match.reverse()
      ans += match
      match=[]
    else:
      ans.append(i)
print(" ".join(map(str, ans)))