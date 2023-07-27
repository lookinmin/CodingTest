# 추월, S1, 구현-문자열

from sys import stdin

n = int(stdin.readline())
start = dict()
end = []

for i in range(n):
    tmp = stdin.readline().rstrip()
    start[tmp] = i

for i in range(n):
    tmp = stdin.readline().rstrip()
    end.append(tmp)

res = 0
for i in range(n-1):
    for j in range(i+1, n):
        if start[end[i]] > start[end[j]]:
            # 앞에 있는 차의 수가 뒤의 수보다 크다 -> 이색기 추월함
            res += 1
            break

print(res)