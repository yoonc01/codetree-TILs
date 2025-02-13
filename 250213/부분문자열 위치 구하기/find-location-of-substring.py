import sys

input = sys.stdin.readline

input_str = input().strip()
target_str = input().strip()

print(input_str.find(target_str))