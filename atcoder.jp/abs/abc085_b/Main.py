N = int(input())
mochis = map(int, [input() for i in range(N)])

print(len(set(mochis)))