def solution(prices):
    answer = []
    for idx in range(len(prices) - 1):
        # stack = []
        cnt = 0
        tmp = prices[idx]       # 현재 값 (기준)
        for i in range(idx + 1, len(prices)):
            cnt += 1
            if prices[i] < tmp:
                break
        answer.append(cnt)
    answer.append(0)
    return answer