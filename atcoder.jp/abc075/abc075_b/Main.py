H, W = map(int, input().split())
M = []
for _ in range(H):
    M.append(input())
 
def check(x:int, y:int) -> int: 
    global H, W, M
    count = 0
    for dx in (x-1, x, x+1):
        for dy in (y-1, y, y+1):
            if dx == x and dy == y:
                continue
            if 0 <= dx < W and 0 <= dy < H and M[dy][dx] == '#':
                count += 1
    return count
 
for y in range(H):
    for x in range(W):        
        if M[y][x] != '#':
            print(check(x, y), end='')
        else:
            print('#', end='')
    print()