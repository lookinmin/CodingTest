from itertools import combinations

def solution(number):
    answer = 0

    arr = list(combinations(number, 3))
    for a in arr:
        if sum(a) == 0:
            answer += 1

    return answer