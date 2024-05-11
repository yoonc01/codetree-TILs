# 변수 선언 및 입력:
n = int(input())

# 입력받은 학생 이름과 점수 변동값을 저장합니다.
changes = [
    input().split()
    for _ in range(n)
]

# 현재 A, B의 점수를 나타냅니다.
score_a, score_b = 0, 0


# 명예의 전당 상태를 반환합니다.
# 총 3가지 상황이 있습니다.
def get_status(score1, score2):
    # 1. A만 명예의 전당에 올라가 있는 경우
    if score1 > score2:
        return 1
    # 2. B만 명예의 전당에 올라가 있는 경우
    elif(score2 > score1):
        return 2
    # 3. A, B 둘 다 명예의 전당에 올라가 있는 경우
    else:
        return 3


ans = 0
# 순서대로 점수를 변동시켜보며
# 조합이 몇 번 변동되는지를 조사합니다.
for name, value in changes:
    value = int(value)
    # 변동이 있는 학생이 A라면
    if name == 'A':
        # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
        # 답을 갱신합니다.
        if get_status(score_a, score_b) != get_status(score_a + value, score_b):
            ans += 1
        
        # 값을 갱신해줍니다.
        score_a += value

    # 변동이 있는 학생이 B라면
    else:
        # 현재 점수와, 이후 점수의 상태를 비교했을 때 조합에 변동이 있다면
        # 답을 갱신합니다.
        if get_status(score_a, score_b) != get_status(score_a, score_b + value):
            ans += 1
        
        # 값을 갱신해줍니다.
        score_b += value

print(ans)