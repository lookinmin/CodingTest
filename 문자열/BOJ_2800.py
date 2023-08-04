# 괄호제거, G5, 문자열

from sys import stdin
from itertools import combinations

data = list(stdin.readline().rstrip())

stack = []
idx = []
res = []

for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)     # 인덱스값을 넣어줌
    elif data[i] == ')':
        idx.append((stack.pop(), i))    # (의 위치와 )의 위치를 같이 넣어줌

for i in range(1, len(idx) + 1):
    com = list(combinations(idx, i))
    # 조합을 통해 제거할 괄호 쌍 뽑아내기
    # 모든 경우의 수를 출력해야되니까
    for c in com:
        tmp = data[:]
        for x, y in c:      # (의 인덱스, )의 인덱스
            tmp[x] = ''     # 해당 인덱스 위치 값 날림
            tmp[y] = ''     # replace써도 될듯
        res.append(''.join(tmp))

res = set(res)  # 중복 문자열 제거
for i in sorted(res):
    print(i)