from collections import Counter

def solution(a):
    if len(a) < 2:
        return 0
    
    counter = Counter(a)
    res = 0
    
    for num in counter:
        if counter[num] * 2 <= res:
            # 현재 체크하는 수의 빈도 * 2 (전체 길이) 가 현재 최대값보다 작음
            continue
            # pass
        
        length = 0
        idx = 0
        
        while idx < len(a) - 1:
            # num이 {0, 1} 중에 위치하고, 다르다 -> idx 증가 + 2(length 증가)
            if (a[idx] == num or a[idx + 1] == num) and (a[idx] != a[idx + 1]):
                length += 2
                idx += 2
            else:
            # 없다 -> 다음꺼 찾기, 길이는 증가 X
                idx += 1
        
        res = max(res, length)
        
    return res