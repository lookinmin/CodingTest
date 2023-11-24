import heapq

def solution(operations):
    answer = []
    q = []
    maxQ = []

    for tmp in operations:
        op = tmp.split(' ')[0]
        value = tmp.split(' ')[1]

        if op == 'I':
            heapq.heappush(q, int(value))
            heapq.heappush(maxQ, (-1 * int(value)))
        else:
            if len(q) == 0:
                pass
            elif value == "1":        # 최댓값 뽑기
                val = -1 * heapq.heappop(maxQ)
                q.remove(val)
            else:                   # 최솟값 뽑기
                val = heapq.heappop(q)
                maxQ.remove(-1*val)

    if len(q) == 0:
        answer = [0,0]
    else:
        answer = [-1 * heapq.heappop(maxQ), heapq.heappop(q)]


    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))