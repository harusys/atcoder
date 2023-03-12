N,K=map(int, input().split())
cnt=0

for x in range(1,N+1):
  for y in range(1,N+1):
    if 1 <= K-(x+y) <= N: cnt += 1

print(cnt)