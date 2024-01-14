def solution(lottos, win_nums):
    answer = []
    cnt = 0  # 맞은 수
    zero = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            cnt += 1

    can_max = zero + cnt
    can_min = cnt

    match_num = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer.append(match_num[can_max])
    answer.append(match_num[can_min])
    return answer