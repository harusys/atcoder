from bisect import bisect_right
 
N = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))
ans = [0] * N

for i in range(N):
  idx = bisect_right(B, A[i])
  ans[len(B) - idx] += 1

print(*ans)