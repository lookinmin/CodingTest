# 에너지 모으기, S1, 완탐-백트래킹

from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
res = 0

def find(s):
    global res
    if len(arr) == 2:
        if s > res:
            res = s
        return
    else:
        for i in range(1, len(arr)-1):
            r = arr[i-1] * arr[i+1]       # r = 선택한 구슬의 전*후 값
            tmp = arr[i]                # 임시 저장

            del arr[i]                  # 선택 구슬 제거
            find(s+r)
            arr.insert(i, tmp)          # 제거했던 구슬을 해당위치에 재배치
                        # 하다보면 길이가 2일때 최대값을 찾아 리턴함

find(0)
print(res)
