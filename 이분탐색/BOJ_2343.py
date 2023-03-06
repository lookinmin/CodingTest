# 기타레슨, S1, 이분탐색

from sys import stdin

N, M = map(int, stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

# mid를 무엇으로 할 것인가?
# m개로 쪼갤 때 사용하는 기준이 되는 합

# 블루레이의 개수가 많음 -> 블루레이 크기를 늘림
# 개수가 적음 -> 블루레이 크기를 줄임         -> 이분탐색

def add():
    cnt = 0         # 비디오 갯수
    sum_video = 0   # 하나의 블루레이에 들어갈 비디오의 합 (개수X, 크기)
    for i in range(N):
        if sum_video + arr[i] > mid:                # 현재 기준값 보다 하나를 추가한 크기가 더 크다면
            cnt += 1                                # 한 블루레이에 들어갈 비디오 수 +1
            sum_video = 0                           # 현재까지 넣은 비디오의 크기 초기화

        sum_video += arr[i]

    else:
        if sum_video != 0:
            cnt += 1

    return cnt

start = max(arr)            # 적어도 하나의 블루레이에 하나의 비디오는 들어가야 하므로 가장 큰 비디오의 크기가 start
end = sum(arr)              # 모든 비디오가 하나의 블루레이에 들어갈 때, 블루레이의 크기가 최대이므로, end = max(arr)

while start <= end:
    mid = (start + end)//2
    cnt = add()
    if cnt <= M:              # 비디오 수가 모자라면
        end = mid - 1           # 크기를 줄인다
    else:                       # 비디오가 많아지면
        start = mid + 1         # 크기를 늘린다.

print(start)                    # 최소 크기 출력
