_, K = map(int, input().split())
S = set(map(int, input().split()))
S.discard(K)
print(min(i for i in range(K+1) if i not in S))