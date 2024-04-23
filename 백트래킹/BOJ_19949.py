# 영재의 시험, S2
from sys import stdin

arr = list(map(int, stdin.readline().split()))

nums = [1, 2, 3, 4, 5]

cnt = 0
total = []
def dfs(depth, correct):
    global cnt
    if depth == 10:
        cnt += 1
        return

    for i in range(5):
        if len(total) < 2 or (total[-2] != total[-1] or total[-1] != nums[i]):
            total.append(nums[i])

            if arr[len(total) - 1] == nums[i]:
                dfs(depth + 1, correct + 1)
            else:
                if len(total) - correct > 5:
                    total.pop()
                    continue
                dfs(depth + 1, correct)
            total.pop()

dfs(0, 0)
print(cnt)