S=input()
N=len(S)
for i in range(0, N, 2):
    print(S[i+1]+S[i], end="")