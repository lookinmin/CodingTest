# 이차원 배열과 연산, G4, 구현-정렬

from sys import stdin

# R : 모든 행에 대해 정렬 (행 수 >= 열 수)
# C : 모든 열에 대해 정렬 (행 수 < 열 수)
# 오름차순 정렬

# r, c, k = map(int, stdin.readline().split())
# r = r-1
# c = c-1

# arr[r][c] == k가 될 시간의 최솟값

arr = [ list(map(int,input().split())) for _ in range(3) ]
cnt = 0

def R():
    global arr
    tmp = []

    for row in arr:
        elem = set(row)
        temt = []       # (수, 개수)
        newRow = []

        for num in elem:
            if num == 0:
                continue
            cnt = row.count(num)
            temt.append((num, cnt))

        temt.sort(key = lambda x : (x[1], x[0]))

        for i in temt:
            newRow.append(i[0])
            newRow.append(i[1])

        newRow = newRow[:100]       # 100개까지만

        tmp.append(newRow)

    max_len = max(map(len, tmp))
    for i in range(len(tmp)):
        while len(tmp[i]) != max_len:
            tmp[i].append(0)

    arr = tmp

for i in range(101):
    try:
        if arr[r][c]==k:
            print(i)
            break
    except:
        pass

    if len(arr[0]) > len(arr):
        arr = list(map(list,zip(*arr)))
        R()
        arr = list(map(list,zip(*arr)))
    else:
        R()

else:
    print(-1)
