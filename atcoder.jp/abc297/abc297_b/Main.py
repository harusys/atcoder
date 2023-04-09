S = list(input())
b1 = S.index('B') + 1
b2 = b1 + S[b1:].index('B') + 1

r1 = S.index('R') + 1
r2 = r1 + S[r1:].index('R') + 1
k = S.index('K') + 1

if (b2-b1) % 2 == 1 and (r1 < k < r2):
  print('Yes')
else:
  print('No')