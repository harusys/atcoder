N,K,A = map(int, input().split())

if (K+A-1)%N==0:
  print(N)
else:
  print((K+A-1)%N)