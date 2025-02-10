import sys

input = sys.stdin.readline

numbers = list(map(float, input().split()))

for number in numbers:
    print(f"{(number * 30.48):.1f}")