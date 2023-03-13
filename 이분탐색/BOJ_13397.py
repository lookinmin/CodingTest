# 구간 나누기 2, G4, 이분탐색
# M개 이하의 구간으로 나누어 구간의 점수의 최댓값을 최소로
# 하나의 구간 = 하나 이상의 연속된 수들
# 배열의 각 수는 모두 하나의 구간에 포함
# 점수 = 구간의 max - min        즉, 최대와 최소의 차이를 작게

from sys import stdin
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

# mid를 뭘로 가져가느냐?

# mid를 각 구간의 max-min 의 최댓값 중 최솟값으로 정의함->답 구하겠다는 소리
def divide(x):
    max_x=min_x=arr[0]                  # 초기값은 그룹이 mid개 일때, 첫번째 원소
    cnt = 1

    for i in range(1, n):
        max_x = max(max_x, arr[i])
        min_x = min(min_x, arr[i])
        if max_x - min_x > x:           # mid값 보다 최대-최소가 크다면 구간 1개 추가
            cnt += 1
            max_x = arr[i]              # 새로 생기는 구간에 대해 max,min 초기화
            min_x = arr[i]
    return cnt


start = 0
end = max(arr)
res = 0

while start <= end:
    mid = (start+end)//2
    if divide(mid) <= m:    # 요구하는 구간의 수보다 작거나 같으면      -> 허용
        end = mid - 1
        res = mid
    else:
        start = mid + 1

print(res)