# 회전 초밥, S1, 브루트 포스
# 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹음 -> 할인
# 1번 행사에 참가할 경우, 쿠폰에 적힌 초밥 하나 무료 제공, 없으면 새로 만듬

from sys import stdin

N, d, k, c= map(int,stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))

start = 0
end = 0
cnt = []
while 1:
    end = start + k
    tmp = set(arr[start : end])

    if c not in tmp and len(tmp) == 4:
        tmp.add(c)

    cnt.append(len(tmp))
    start += 1

    if end == N:
        end = 0
        start = end + k     # 여기서 tmp를 바꿔줘야 되는데 어캐하는지 모르겠음

    if start == N:      # 한바퀴 돌았다
        break

print(max(cnt))

#-----------------------------------------------

from sys import stdin

N, d, k, c= map(int,stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))

start = 0
end = 0
res = 0
while start != N:
    end = start + k
    case = set()
    addable = True
    for i in range(start, end):
        i %= N
        case.add(arr[i])
        if arr[i] == c:
            addable = False
    cnt = len(case)
    if addable:
        cnt += 1
    res = max(res, cnt)

    start += 1

print(res)