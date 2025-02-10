import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))

for number in numbers:
    print(number + 2)
