# 꿀 따기, G5, 누적합, 그리디

from sys import stdin


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
psum = [0] * (n+1)
psum[0] = arr[0]

# 1. 벌 - 벌 - 꿀 순서인 경우, 첫번째 벌은 무조건 맨 끝, 꿀통은 무조건 맨 마지막
# 2. 꿀 - 벌 - 벌 도 마찬가지
# 3. 벌 - 꿀 - 벌 인 경우, 벌은 양쪽 끝에 위치, 꿀 위치만 바꿔가면서 확인

for i in range(1, n):       # 일단 누적합으로 모두 담기
    psum[i] = psum[i-1] + arr[i]

# 1
res = 0
for i in range(1, n-1):     # 우측끝이 벌통이니까 n-1까지
    res = max(res, psum[n-2] + psum[i-1] - arr[i])

# 2
for i in range(1, n-1):
    res = max(res, psum[n-1] - arr[0] + psum[n-1] - psum[i] - arr[i] )
    # 총합 - 꿑통(첫번째) + 끝까지(맨 오른쪽 벌) - 현재 중간 벌 위치까지의 누적합(2번 더해졌으니까) - 현재 중간 벌의 위치의 값

# 3
for i in range(1, n-1):
    res = max(res, psum[n-2] - arr[0] + arr[i])
    # 맨 마지막 안되니까 그 전까지의 합 - 첫번째에도 벌 위치했으니까 빼고 + 변화하는 꿀통의 위치

print(res)