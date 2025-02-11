import sys

input = sys.stdin.readline

numbers = list(input().split())
print("".join(numbers[::-1]))