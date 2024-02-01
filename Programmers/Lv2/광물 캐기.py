def solution(picks, minerals):
    answer = 0
    # 한 곡괭이당 5개가 최대
    # picks = [dia, iron, stone]

    sumPicks = sum(picks)
    # 총 갯수

    canGet = sumPicks * 5  # 총 캘 수 있는 광물 수
    if len(minerals) > canGet:
        minerals = minerals[:canGet]

    cnt = [[0, 0, 0] for _ in range(10)]  # 5개 당 각 광물이 몇개씩 있는 지
    # minerals의 길이의 최대가 50, 5개씩 나누면 10번이 최대
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt[i // 5][0] += 1
        elif minerals[i] == 'iron':
            cnt[i // 5][1] += 1
        else:
            cnt[i // 5][2] += 1

    cnt.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    # 다이아가 많은 광물 모음 순으로 정렬

    for arr in cnt:
        for i in range(len(picks)):
            if i == 0 and picks[i] > 0:  # dia 먼저
                picks[i] -= 1
                answer += sum(arr)  # 어차피 다 1 필요
                break
            elif i == 1 and picks[i] > 0:  # iron
                picks[i] -= 1
                answer += arr[0] * 5 + arr[1] + arr[2]
                break
            elif i == 2 and picks[i] > 0:
                picks[i] -= 1
                answer += arr[0] * 25 + arr[1] * 5 + arr[2]
                break

    return answer