import sys

input = sys.stdin.readline

numbers = input().split()
print("".join(numbers[::-1]))