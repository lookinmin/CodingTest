# 숫자고르기, G5, 그래프 - dfs
# 사이클 확인 문제
# 사이클 확인 -> 해당 사이클 구성 노드들을 찾는게 정답

from sys import stdin
import sys
sys.setrecursionlimit(10**6)

n = int(stdin.readline())
arr = [0]
for i in range(n):
    arr.append(int(input()))

res = set()     # 결과 담을 set

def dfs(top, bottom, v):
    top.add(v)              # 값 자체를 top에 추가
    bottom.add(arr[v])      # 값의 인덱스를 bottom에 추가
    if arr[v] in top:               # arr[v]가 top에 있을 때
        if top == bottom:           # 두 집합이 같다면
            res.update(top)         # 현재 top으로 res를 업데이트
            return True
        return False
    return dfs(top, bottom, arr[v])     # 아니라면 다음 dfs()

for i in range(1, n+1):
    if i not in res:
        dfs(set(), set(), i)

print(len(res))
for i in sorted(list(res)):
    print(i)

