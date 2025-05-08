dirs = input()

direction = 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = 0, 0
for cmd in dirs:
    if cmd == "F":
        x = x + dxs[direction]
        y = y + dys[direction]
    elif cmd == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

print(x, y)
        
