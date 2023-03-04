# 빗물, G5, 구현-시물레이션

from sys import stdin

h, w = map(int, stdin.readline().split())

arr = list(map(int, stdin.readline().split()))

res = 0
for i in range(1, w-1):
    left_max = max(arr[:i])             # 나 기준 왼쪽에서 제일 높은 기둥
    right_max = max(arr[i+1:])          # 나 기준 오른쪽에서 가장 높은 기둥
    tmp = min(left_max, right_max)      # 그 둘 중에 더 작은거만큼

    if arr[i] < tmp:        # 고일 수 있음(움푹 들어가있는 부분)
        res += tmp - arr[i]     # 나 기준으로 나랑 더 낮은 기둥만큼의 높이 차이만큼 물이 들어참

print(res)