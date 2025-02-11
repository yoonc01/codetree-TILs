import sys

input = sys.stdin.readline

h, m = input().split(":")

h = int(h) + 1

print(f"{h}:{m}")