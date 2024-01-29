def solution(n, times):
    answer = 0
    start = min(times)
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2

        tmp = 0
        for num in times:
            tmp += (mid // num)

            if tmp >= n:  # 검사 끝, for문 더 돌 필요 X
                break

        if tmp >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer