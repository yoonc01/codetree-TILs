import sys

input = sys.stdin.readline

n = int(input())
B = [input().strip() for _ in range(n)]

d = {"H": 0, "S": 1, "P": 2}

def get_score(a_choice, b_choice):
    a_choice = d[a_choice]
    b_choice = d[b_choice]

    if (a_choice - b_choice + 3) % 3 == 2:
        return (1)
    else:
        return (0)

rock_left = [0 for _ in range(n)]
sciccer_left = [0 for _ in range(n)]
paper_left = [0 for _ in range(n)]

rock_right = [0 for _ in range(n)]
sciccer_right = [0 for _ in range(n)]
paper_right = [0 for _ in range(n)]

rock_left[0] = get_score("H", B[0])
sciccer_left[0] = get_score("S", B[0])
paper_left[0] = get_score("P", B[0])

rock_right[n - 1] = get_score("H", B[n - 1])
sciccer_right[n - 1] = get_score("S", B[n - 1])
paper_right[n - 1] = get_score("P", B[n - 1])

for i in range(1, n):
    rock_left[i] = rock_left[i - 1] + get_score("H", B[i])
    sciccer_left[i] = sciccer_left[i - 1] + get_score("S", B[i])
    paper_left[i] = paper_left[i - 1] + get_score("P", B[i])
    
    rock_right[n - 1 - i] = rock_right[n - i] + get_score("H", B[n - 1 - i])
    sciccer_right[n - 1 - i] = sciccer_right[n - i] + get_score("H", B[n - 1 - i])
    paper_right[n - 1 - i] = paper_right[n - i] + get_score("H", B[n - 1 - i])

ans = 0
for i in range(0, n - 1):
    ans = max(ans, rock_left[i] + sciccer_right[i + 1])
    ans = max(ans, rock_left[i] + paper_right[i + 1])
    ans = max(ans, sciccer_left[i] + rock_right[i + 1])
    ans = max(ans, sciccer_left[i] + paper_right[i + 1])
    ans = max(ans, paper_left[i] + rock_right[i + 1])
    ans = max(ans, paper_left[i] + sciccer_right[i + 1])

print(ans)    
    
    
    
    
