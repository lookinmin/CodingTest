from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        target = q.popleft()  # 기준
        cnt = 0

        for num in q:
            cnt += 1
            if target > num:  # 더 크면 끝
                break
        answer.append(cnt)

    return answer