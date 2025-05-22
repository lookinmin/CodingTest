def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        scheduled_time = schedules[i]  # 출근 희망 시각
        # 시간과 분으로 분리
        scheduled_hour = scheduled_time // 100
        scheduled_min = scheduled_time % 100
        
        # 마감 시각 계산 (10분 추가)
        deadline_min = scheduled_min + 10
        deadline_hour = scheduled_hour + (deadline_min // 60)
        deadline_min = deadline_min % 60
        deadline_time = deadline_hour * 100 + deadline_min
        
        is_valid = True
        
        # 7일 동안 체크
        for day in range(7):
            current_day = (startday + day) % 7
            
            # 주말은 체크하지 않음
            if current_day in [0, 6]:  # 일요일(0) 또는 토요일(6)
                continue
                
            # 평일 출근 시간 체크
            actual_time = timelogs[i][day]
            if actual_time > deadline_time:
                is_valid = False
                break
        
        if is_valid:
            answer += 1
            
    return answer