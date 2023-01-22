N, A, B = map(int, input().split())
cnt = 0

for num in range(1, N+1):
    if A <= sum(list(map(int, list(str(num))))) <= B:
        cnt += num

print(cnt)