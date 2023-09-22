# 삼각형 만들기, S3, 정렬

from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline().rstrip()))

arr.sort(reverse=True)

# 삼각형 조건
# 두 변의 길이의 합 > 나머지 한 변의 길이

idx = 0

while 1:
    if idx == n-2:
        print(-1)
        break
    long = arr[idx]
    others = arr[idx+1] + arr[idx+2]
    if long < others:
        print(long+others)
        break
    else:
        idx += 1
