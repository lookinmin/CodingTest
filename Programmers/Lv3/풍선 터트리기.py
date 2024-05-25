def solution(a):
    answer = 0
    # 왼쪽 or 오른쪽 방향에 큰 수만 존재 -> 남김
    res = [0] * len(a)
    front = int(1e9)
    back = int(1e9)
    
    for i in range(len(a)):
        if a[i] < front:
            front = a[i]
            res[i] = 1
        if a[-1-i] < back:
            back = a[-1-i]
            res[-1-i] = 1 
        
    return sum(res)