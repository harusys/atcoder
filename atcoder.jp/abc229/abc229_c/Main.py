N,W=map(int,input().split())
AB=[tuple(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda t: -t[0])
ans=0
for A,B in AB:
    u = min(B,W)
    W -= u
    ans += A * u
    if W == 0:
        break
print(ans)