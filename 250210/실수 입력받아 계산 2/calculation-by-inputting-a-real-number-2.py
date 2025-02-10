import sys

input = sys.stdin.readline

numbers = list(map(float, input().split()))

for number in numbers:
    print(f"{(number + 1.5):.2f}")