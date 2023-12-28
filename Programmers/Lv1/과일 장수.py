from collections import deque

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    score = deque(score)

    while score:
        tmp = []
        for i in range(m):
            if score:
                tmp.append(score.popleft())
            else:
                break

        if len(tmp) < m:
            answer += 0
        else:
            answer += (min(tmp) * m)

    return answer