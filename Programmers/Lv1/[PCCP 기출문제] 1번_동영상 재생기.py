def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    return "{:02d}:{:02d}".format(seconds // 60, seconds % 60)


def solution(video_len, pos, op_start, op_end, commands):
    # 동영상 길이, 직전 재생위치, 오프닝 시작, 끝, 사용자 입력
    # 사용자 입력 끝난 후의 동영상 위치 리턴
    
    # next : +10s
    # prev : -10s
    video_end = time_to_seconds(video_len)
    op_st = time_to_seconds(op_start)
    op_ed = time_to_seconds(op_end)
    
    now = time_to_seconds(pos)
    for command in commands:
        if op_st <= now <= op_ed:
            now = op_ed
        
        if command == 'prev':
            # -10
            now = max(0, now - 10)
        else:
            # +10
            now = min(video_end, now + 10)
    
    if op_st <= now <= op_ed:
        now = op_ed
    
    return seconds_to_time(now)