import heapq

def solution(n, works):
    answer = 0
    # 야근을 시작한 시점 + 남은 일의 작업량 ^ 2
    # 1시간동안 작업량 1
    # 총 가능 작업시간 n

    if sum(works) <= n:
        return 0

    works = [-work for work in works]
    heapq.heapify(works)

    while n > 0 and works:
        max_work = -heapq.heappop(works)
        max_work -= 1
        heapq.heappush(works, -max_work)
        n -= 1

    for i in works:
        answer += i ** 2
    return answer

# 매번 정렬해서 가장 큰 수에서 -1 씩 할때
# 정렬에서 발생하는 시간 복잡도 문제를 heapq를 통해 해결