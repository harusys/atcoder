T = int(input())

def f():
  x = list(map(int, input().split()))
  x.sort()
  x1 = x[1] - x[0]
  x2 = x[2] - x[1]

  d = min(x1,x2) // 2

  if x1 % 2 != 0 or x2 % 2 != 0 or (max(x1,x2)-2*d) % 3 != 0:
    return -1

  return d + (max(x1,x2)-2*d) // 3

for _ in range(T):
  print(f())