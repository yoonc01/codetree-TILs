n = int(input())

for i in range(1, n + 1):
    arr = [0 for _ in range(n)]
    for j in range(1, n + 1):
        arr[j - 1] = f"{i} * {j} = {i * j}"
    print(", ".join(arr))