import sys

input = sys.stdin.readline

m, d, y = input().replace("-", " ").split()
print(f"{y}.{m}.{d}")