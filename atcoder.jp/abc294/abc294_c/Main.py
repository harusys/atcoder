n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)

def search(x):
	L = 0
	R = n+m-1
	while L <= R:
		M = (L + R) // 2
		if x < C[M]:
			R = M - 1
		if x == C[M]:
			return M
		if x > C[M]:
			L = M + 1
	return -1 

for a in A:
  print(search(a) + 1, end=" ")
print()
for b in B:
  print(search(b) + 1, end=" ")