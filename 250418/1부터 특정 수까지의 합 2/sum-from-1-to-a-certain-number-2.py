n = int(input())

def get_total(n):
    if n == 1:
        return 1
    return get_total(n - 1) + n

print(get_total(n))