x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

min_x, min_y = min(x1, x2, a1, a2), min(y1, y2, b1, b2)
max_x, max_y = max(x1, x2, a1, a2), max(y1, y2, b1, b2)

print((max_y - min_y) * (max_x - min_x))