from itertools import combinations
def solution(numbers):
    answer = []
    tmp = list(combinations(numbers, 2))
    for w in tmp:
        t = w[0] + w[1]
        answer.append(t)
    answer = list(set(answer))
    answer.sort()
    return answer