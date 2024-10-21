from collections import deque

def time_cvt(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def cvt_time(minutes):
    h = minutes // 60
    m = minutes % 60
    return "{:02}:{:02}".format(h, m)

def solution(n, t, m, timetable):
    answer = ''
    # n : 몇 회
    # t : 간격
    # m : 몇 명
    # 첫 출발 시각 : "09:00" = 540
    
    crew_times = sorted([time_cvt(time) for time in timetable])
    
    time = 540
    q = deque(crew_times)
    
    last = 0
    
    for i in range(n):
        cnt = 0
        last_time = 0
        
        while q and q[0] <= time and cnt < m:
            last_time = q.popleft()
            cnt += 1
        
        if i == n - 1:  # 마지막 셔틀
            if cnt < m:
                last = time
            else:
                last = last_time - 1
        
        time += t
    
    answer = cvt_time(last)
    return answer