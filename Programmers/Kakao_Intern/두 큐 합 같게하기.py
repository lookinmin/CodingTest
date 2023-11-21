from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    sumQ1 = sum(q1)
    sumQ2 = sum(q2)

    if (sumQ1 + sumQ2) % 2 != 0:
        return -1

    limit = len(q1) * 3
    # 무한으로 돌지 않게

    while 1:
        if sumQ1 > sumQ2:
            tmp = q1.popleft()
            q2.append(tmp)
            sumQ1 -= tmp
            sumQ2 += tmp
            answer += 1
        elif sumQ1 < sumQ2:
            tmp = q2.popleft()
            q1.append(tmp)
            sumQ2 -= tmp
            sumQ1 += tmp
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break

    return answer
