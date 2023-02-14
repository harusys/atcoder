T=int(input())
for i in range(T):
  cnt=0
  _=input()
  A=map(int,input().split())
  for a in A:
    if a%2 == 1:
      cnt += 1
  print(cnt)