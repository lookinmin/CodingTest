from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)

    while q:
        m = max(q)
        n = q.popleft()

        location -= 1

        if n != m:  # 제일 큰 수가 아님
            q.append(n)
            if location < 0:
                location = len(q) - 1
        else:
            answer += 1
            if location < 0:
                break

    return answer


def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while 1:
        cur = queue.pop(0)       # cur = [번호, 우선순위]
        if any(cur[1] < q[1] for q in queue):       # queue안에 어떤 수의 우선순위가 현재 우선순위보다 높은게 존재하면 True
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print( solution([1, 1, 9, 1, 1, 1], 0))