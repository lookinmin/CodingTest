# Contact, G5, 문자열-정규표현식

from sys import stdin
import re       # 정규표현식을 위해
# (100+1+ | 01)+ = {1001, 01, 100101, 011001, 10001, ... }

# 파이썬 re 정규표현식은
# +, (), | 를 제공

T = int(stdin.readline())
res = []
for _ in range(T):
    arr = stdin.readline().strip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(arr)
    if m:
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)
