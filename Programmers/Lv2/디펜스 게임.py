import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)

    q = []

    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        # 힙 내부의 사람 수 만큼 k를 쓰면 됨
        if len(q) > k:
            last = heapq.heappop(q)
            if last > n:
                return i  # 더이상 라운드 진행 불가
            n -= last

    return len(enemy)