import heapq
def solution(scoville, K):

    cnt = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        minx = heapq.heappop(scoville)
        miny = heapq.heappop(scoville)
        tmp = minx + (miny * 2)
        heapq.heappush(scoville, tmp)
        cnt += 1

        if len(scoville) == 1 and scoville[0] < K:      # 이 조건을 생각을 못했네 시이이이발
            return -1

    return cnt

print(solution([1, 2, 3, 9, 10, 12]	, 7))