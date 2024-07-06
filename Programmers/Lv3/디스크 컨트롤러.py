import heapq
def solution(jobs):
    jobs.sort() # 들어온 기준으로 정렬
    k = len(jobs)
    q = []
    answer = []
    
    now = 0
    while len(answer) != k:
        while jobs and now >= jobs[0][0]:
            spot, time = jobs.pop(0)
            heapq.heappush(q, (time, spot))
            # 소요 순으로 힙 구현
        
        if jobs and q == []:
            spot, time = jobs.pop(0)
            now = spot
            heapq.heappush(q, (time, spot))
        
        time, spot = heapq.heappop(q)
        now += time
        answer.append(now - spot)
        
    return sum(answer) // len(answer)