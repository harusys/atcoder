N,T = map(int, input().split())
C = [0]+list(map(int, input().split()))
R = [0]+list(map(int, input().split()))

if T in set(C):
  color = T
else:
  color = C[1]

ans = 0
for i in range(1,N+1):
  if C[i] == color and R[ans] < R[i]:
    ans = i
print(ans)