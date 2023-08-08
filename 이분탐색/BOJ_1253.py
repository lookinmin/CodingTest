# 좋다, G4, 이분탐색

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort()
# 어떤 수를 다른 두수의 합으로 나타내야됨
# 2번째 수까진 죽어도 만들 수 없음
cnt = 0
# 수에 음수가 포함될 수 있음...

for i in range(n):

    tmp = arr[:i] + arr[i+1:]       # 현재 찾아야하는 값을 제외한 나머지 값들
    s = 0
    e = len(tmp) - 1

    while s < e:
        mid = tmp[s] + tmp[e]
        if mid == arr[i]:
            cnt += 1
            break
        elif mid < arr[i]:
            s += 1
        else:
            e -= 1

print(cnt)
# for i in range(2, n):
#     s = 0
#     e = i-1
#     while 1:
#         if arr[s] + arr[e] == arr[i]:
#             cnt += 1
#             break
#         elif arr[s] + arr[e] > arr[i]:
#             e -= 1
#         elif arr[s] + arr[e] < arr[i]:
#             e += 1
