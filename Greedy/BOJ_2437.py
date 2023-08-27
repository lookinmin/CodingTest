# 저울, G2, 그리디

from sys import stdin

# 측정할 수 없는 무게 중 최소값

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort()

# 구간합으로 생각하기



target = 1          # 자연수 범위 내이므로 1부터
for i in arr:
    if target < i:
        break
    target += i
print(target)