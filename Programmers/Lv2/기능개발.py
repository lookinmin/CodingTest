from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    speeds = deque(speeds)

    time = 0
    cnt = 0
    while q:
        if q[0] + time * speeds[0] >= 100:
            q.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)

    return answer