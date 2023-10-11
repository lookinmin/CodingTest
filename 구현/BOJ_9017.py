# 크로스 컨트리, S4, 구현

from sys import stdin

# 6명이 안되면 팀으로 치지 않는다
# 상위 4명의 점수 합산으로 한다
# 4명 점수 합이 같다면 5번째 선수의 점수로 체크한다

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    teams = dict()

    for num in arr:     # 일단 사람부터
        if num in teams:
            teams[num] += 1
        else:
            teams[num] = 1

    score = dict()
    idx = 1

    for num in arr:
        if teams[num] == 6:
            if num in score:
                if score[num][0] < 4:
                    score[num][0] += 1
                    score[num][1] += idx
                elif score[num][0] == 4:
                    score[num][0] += 1
                    score[num][2] = idx
            else:
                score[num] = [1, idx, 0]
            idx += 1

    res = sorted(score.items(), key = lambda x : (x[1][1],x[1][2]))
    print(res[0][0])