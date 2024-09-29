from collections import deque, defaultdict

weight = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
]

def solution(numbers):
    n = len(numbers)
    numbers = list(map(int, numbers))
    dp = defaultdict(lambda : float('inf'))
    dp[(4, 6, 0)] = 0
    # 초기 상태 (left, right, index)
    
    q = deque([(4, 6, 0)])
    
    while q:
        left, right, idx = q.popleft()
        if idx == n:     # 다 함
            continue
        
        nxt_num = numbers[idx]
        
        if nxt_num != right:    # 왼손 이동
            cost = dp[(left, right, idx)] + weight[left][nxt_num]
            if cost < dp[(nxt_num, right, idx + 1)]:
                dp[(nxt_num, right, idx + 1)] = cost
                q.append((nxt_num, right, idx + 1))
                
        if nxt_num != left:
            cost = dp[(left, right, idx)] + weight[right][nxt_num]
            if cost < dp[(left, nxt_num, idx + 1)]:
                dp[(left, nxt_num, idx + 1)] = cost
                q.append((left, nxt_num, idx + 1))
                
    return min(dp[(left, right, n)] for left in range(10) for right in range(10))