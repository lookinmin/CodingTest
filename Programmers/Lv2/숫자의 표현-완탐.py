def solution(n):
    answer = 1  # 자연수 그자체
    for i in range(1, n):
        tmp = 0
        for j in range(i, n):
            tmp += j

            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break

    return answer