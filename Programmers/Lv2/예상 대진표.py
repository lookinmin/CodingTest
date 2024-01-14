def solution(n, a, b):
    answer = 0
    cnt = 0
    while 1:
        cnt += 1
        min_num = min(a, b)
        max_num = max(a, b)
        if min_num % 2 != 0 and min_num + 1 == max_num:
            return cnt
        a = (a + 1) // 2
        b = (b + 1) // 2
