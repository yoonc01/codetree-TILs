import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))

print(sum(numbers))