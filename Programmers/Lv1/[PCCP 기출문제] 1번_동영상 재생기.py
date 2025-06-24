def solution(video_len, pos, op_start, op_end, commands):
    # 동영상 길이, 직전 재생위치, 오프닝 시작, 끝, 사용자 입력
    # 사용자 입력 끝난 후의 동영상 위치 리턴
    
    # next : +10s
    # prev : -10s
    end = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
    op_st = int(op_start.split(':')[0]) * 60 + int(op_start.split(':')[1])
    op_ed = int(op_end.split(':')[0]) * 60 + int(op_end.split(':')[1])
    
    now_min = int(pos.split(':')[0])
    now_sec = int(pos.split(':')[1])
    
    now = now_min * 60 + now_sec
    for com in commands:
        if op_st <= now <= op_ed:
            now = op_ed
        
        if com == 'prev':
            # -10
            if now - 10 >= 0:
                now -= 10
            else:
                now = 0
        else:
            # +10
            if now + 10 <= end:
                now += 10
            else:
                now = end
    
    if op_st <= now <= op_ed:
        now = op_ed
    
    ans_min = now // 60
    ans_sec = now % 60
    answer = "{:02d}:{:02d}".format(ans_min, ans_sec)
    return answer