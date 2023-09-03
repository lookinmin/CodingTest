# 괄호 추가하기, G3, 구현-완탐

from sys import stdin
n = int(stdin.readline())
data = list(stdin.readline().rstrip())
# 수는 0~9, 연산은 +, -, *
# 수식 계산 eval()

# 부분 부분 계산을 통해 dfs()로 탐색한다

res = float('-inf')

def dfs(idx, value):
    global res

    if n == idx:
        res = max(res, int(value))
        return

    if idx + 4 <= n:        # ( ) 를 껴넣음
        dfs(idx+4, str(eval(''.join([value, data[idx]] + [str(eval(''.join(data[idx+1 : idx+4])))]))))
    if idx + 2 <= n:        # 괄호 사용하지 않음
        dfs(idx+2, str(eval(''.join([value] + data[idx: idx+2]))))


dfs(1, data[0])
print(res)