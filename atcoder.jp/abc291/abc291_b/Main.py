N=int(input())
X=[*map(int,input().split())]
X=sorted(X)[N:-N]
print(sum(X)/len(X))