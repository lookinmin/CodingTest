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

# -------------------------

from collections import deque
def solution(progresses, speeds):
    q = deque(progresses)
    speeds = deque(speeds)
    res = []
    
    while q:
        day = (100 - q[0] + speeds[0] - 1) // speeds[0]
        # 첫번째 작업이 완료되기 까지 걸리는 시간
        cnt = 0
        
        while q and (q[0] + speeds[0] * day) >= 100:
            # 이후 작업들도 해당 day 내 작업 완료 가능하다면
            q.popleft()
            speeds.popleft()
            cnt+=1
            # 추가
            
        res.append(cnt)

    return res