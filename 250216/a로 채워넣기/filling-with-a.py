import sys

input = sys.stdin.readline

string = input().strip()

strArray = list(string)

strArray[1] = 'a'
strArray[len(strArray) - 2] = 'a'

print("".join(strArray))