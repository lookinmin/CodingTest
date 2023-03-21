# 센서, G5, 그리디
# 각 집중국의 수신 가능 영역 길의 합 최소화


from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr = sorted(arr)

# k과 n이 같다면, 답은 0
# 센서들 간의 거리를 계산 -> 내림차순 정렬

if k >= n:
    print(0)
    exit(0)

dist = []
for i in range(1, n):
    dist.append(arr[i] - arr[i-1])

dist.sort(reverse=True)

# 센서들을 k개의 구간으로 나눠야 하므로 k-1번 만큼 반복하면서 큰 값 제거
# 최소한이니까

for _ in range(k-1):
    dist.pop(0)

print(sum(dist))