N, M = map(int, input().split())
S = [input()[-3:] for i in range(N)]
T = [input() for i in range(M)]
count = 0
for s in S:
  if s in T:
    count += 1
print(count)