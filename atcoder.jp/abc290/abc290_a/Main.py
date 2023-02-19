_,M=map(int,input().split())
A=list(map(int,input().split()))
B=map(int,input().split())
total=0
for i in B:
  total+=A[i-1]
print(total)