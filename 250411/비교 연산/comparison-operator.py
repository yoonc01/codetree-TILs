a, b = map(int, input().split())

def condition(con):
    if con:
        print(1)
    else:
        print(0)

condition(a >= b)
condition(a > b)
condition(b >= a)
condition(b > a)
condition(a == b)
condition(a != b)
