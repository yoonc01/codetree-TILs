import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))

for number in numbers:
    print(f"Your score is {number} point.")
