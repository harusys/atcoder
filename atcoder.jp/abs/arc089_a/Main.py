N = int(input())
t_old, x_old, y_old = 0, 0, 0

for i in range(N):
    t, x, y = map(int,input().split())
    # Movable distance:  (must: <timespan)
    # Non stop: x+y, t | same even-odd
    timespan = abs(t_old - t)
    dist = abs(x_old - x) + abs(y_old - y)
    if timespan < dist or (x + y + t) % 2:
        print("No")
        exit()
    t_old = t
    x_old = x
    y_old = y
print("Yes")