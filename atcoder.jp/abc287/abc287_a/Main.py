N = int(input())
count = 0
for i in range(N):
    if input() == "For":
        count += 1
if count > N / 2:
  print('Yes')
else:
  print('No')