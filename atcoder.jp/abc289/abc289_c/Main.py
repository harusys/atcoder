import itertools
N,M=map(int,input().split())
S=[]
cnt=0
for i in range(M):
  _=input()
  S.append(input().split())
for j in range(1,M+1):
  for t in itertools.combinations(S, j):
    flat = set(list(itertools.chain.from_iterable(t)))
    if len(flat)==N:
      cnt += 1
print(cnt)