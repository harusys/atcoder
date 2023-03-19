H,W = map(int, input().split())
A = [ [0] * W for i in range(H) ]
for i in range(H):
  A[i] = list(map(int, input().split()))

for i in range(H):
  for j in range(W):
    a = A[i][j]
    if a == 0:
      print(".", end="")
    else:
      print(chr(a+64), end="")
  print()