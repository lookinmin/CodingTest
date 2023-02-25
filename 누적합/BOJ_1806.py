# 부분합, G4, 누적합 - 투포인터
# 합이 S 이상, 가장 짧은 것

from sys import stdin

n, s = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
i,j = 0,0       # 투 포인터 초기화
psum = arr[0]       # 부분합
res = 100001

while 1:
    if psum >= s:
        psum -= arr[i]      # 왼쪽 포인터를 땡기면서
        res = min(res, j - i + 1)       # 더 작은 값으로 최신화
        i += 1
    else:
        j += 1              # 오른쪽으로 한칸 씩 밀면서
        if j == n:          # 끝까지갔으면 탈출
            break
        psum += arr[j]      # 부분합 증가

if res == 100001:
    print(0)
else:
    print(res)