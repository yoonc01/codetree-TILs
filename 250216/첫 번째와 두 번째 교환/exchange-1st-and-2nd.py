string = input()

strArray = list(string)

first = strArray[0]
second = strArray[1]

for i in range(len(string)):
    if (strArray[i] == first):
        strArray[i] = second
    elif (strArray[i] == second):
        strArray[i] = first

print("".join(strArray))