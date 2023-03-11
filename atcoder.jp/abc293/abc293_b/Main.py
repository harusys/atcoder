N = int(input())
A = [*map(int, input().split())]
called = [0] * N
 
for i in range(N):
  if called[i] == 0:
    called[A[i] - 1] = 1

print(N - sum(called))
print(*[i+1 for i, x in enumerate(called) if x == 0])