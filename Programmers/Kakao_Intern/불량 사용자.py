from itertools import permutations


def check(unit, banned_id):
    for i in range(len(unit)):
        if len(unit[i]) != len(banned_id[i]):
            # 1. 길이부터 비교
            return False
        for j in range(len(unit[i])):
            if unit[i][j] != banned_id[i][j] and banned_id[i][j] != '*':
                return False

    return True


def solution(user_id, banned_id):
    answer = []

    for unit in permutations(user_id, len(banned_id)):
        if check(unit, banned_id):
            if set(unit) not in answer:
                answer.append(set(unit))

    return len(answer)