from sys import stdin
from collections import deque

arr = list(map(int, stdin.readline().split()))
n = int(stdin.readline())
tmp = list(map(int, stdin.readline().split()))

res = int(1e9)

for i in range(n):
    cnt = 0
    part = arr.copy()
    belt = deque(tmp.copy())

    while sum(part) > 0:
        cnt += 1

        if part[belt[i]-1] > 0:
            part[belt[i]-1] -= 1

        k = belt.popleft()
        belt.append(k)

        if cnt == len(belt) and sum(part) > 0:        # 개수만큼 돌면 전부 못얻음
            cnt = -1
            break

    res = min(res, cnt)
    if res == -1:
        break

print(res)

# 시간복잡도 : O(n)
# 바깥쪽 for 루프가 n번 실행되는데, 내부 while은 최대 100번
# 공간복잡도 : O(1)
# arr, tmp의 길이의 최대가 각각 100이라 했을 때,
# part, belt는 복사본이므로 역시 100
# res, cnt는 상수 공간
# 즉, O(100) + O(100) = O(1)