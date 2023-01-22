N = int(input())
A = list(map(int, input()))
B = list(map(int, input()))

for i in range(N):
    if A[i] > B[i]:
        A[i], B[i] = B[i], A[i]

total = int("".join(map(str, A))) * int("".join(map(str, B)))

print(total % 998244353)
