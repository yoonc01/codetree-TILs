n = int(input())

l = list(map(int, input().split()))

ans = 0
while(len(l) != 1):
    l.sort(reverse = True)
    a = l.pop()
    b = l.pop()
    ans = ans + a + b
    l.append(a + b)

print(ans)