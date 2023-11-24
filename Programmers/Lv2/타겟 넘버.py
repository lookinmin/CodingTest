from collections import deque

def solution(numbers, target):
    answer = 0

    n = len(numbers)

    q = deque()
    q.append([numbers[0], 0])   # 값, idx
    q.append([-1 * numbers[0], 0])


    while q:
        now, idx = q.popleft()
        idx += 1

        if idx < n:
            q.append([now + numbers[idx], idx])
            q.append([now - numbers[idx], idx])
        else:
            if now == target:
                answer += 1

    return answer

print(solution([1,1,1,1,1], 3))