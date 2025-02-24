n = int(input())

number = []
def printCnt(n):
    if n == 0:
        return
    number.append(n)
    printCnt(n - 1)
    number.append(n)

printCnt(n)
print(" ".join(map(str, number)))