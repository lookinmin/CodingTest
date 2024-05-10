from collections import deque

def cvt_time(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def solution(plans):
    answer = []
    plans = [(a, cvt_time(b), int(c)) for a, b, c in plans]
    plans = sorted(plans, key=lambda x: x[1])
    q = deque()
    term = 0  # 지금 시작시간, 다음수업 시작시간 간 간격
    for i in range(len(plans)):
        now, start, playtime = plans[i]

        while q:
            name, left_time = q.pop()
            if term >= left_time:
                term -= left_time
                answer.append(name)
            else:
                q.append([name, left_time - term])
                break

        q.append([now, playtime])

        if i < len(plans) - 1:
            nxt = plans[i + 1][1]
            term = nxt - start

    while q:
        name, _ = q.pop()
        answer.append(name)

    return answer