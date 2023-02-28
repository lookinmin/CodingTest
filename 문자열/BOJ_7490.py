# 0만들기,G5, 문자열-백트래킹

# 재귀함수를 통한 백트래킹

from sys import stdin
import copy

def recur(arr, n):
    if len(arr) == n:
        operators.append(copy.deepcopy(arr))
        return
    arr.append(' ')     # 공백
    recur(arr, n)
    arr.pop()

    arr.append('+')
    recur(arr, n)
    arr.pop()

    arr.append('-')
    recur(arr, n)
    arr.pop()

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    operators = []      # 연산자가 들어올 빈 배열 선언
    recur([], n-1)

    for op in operators:        # 모든 연산자 가능 경우의 수가 들어있는 배열들
        res = ''
        for i in range(n-1):        # n==3이면, 1~2
            res += str(i+1) + op[i]
        res += str(n)       # 마지막 수
        if eval(res.replace(' ', '')) == 0:         # eval() -> 문자열로 작성된 코드를 그대로 실행
            print(res)                              # 값이 0일때만 출력
    print()