def get_total(n):
    if n == 0 or n == 1:
        return n
    return n + get_total(n - 2)

n = int(input())

print(get_total(n))