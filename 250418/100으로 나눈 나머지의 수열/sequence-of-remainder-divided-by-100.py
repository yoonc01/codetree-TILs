def calc(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    
    return (calc(n - 1) * calc(n - 2)) % 100

n = int(input())

print(calc(n))