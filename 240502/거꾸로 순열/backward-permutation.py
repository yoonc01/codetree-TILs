def backtrack(ans, n, num):
    if n == 0:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(num, 0, -1):
        if i in ans:
            continue
        ans.append(i)
        backtrack(ans, n - 1, num)
        ans.pop()

n = int(input())

backtrack([], n, n)