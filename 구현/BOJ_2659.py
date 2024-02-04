# S3, 십자카드 문제
from collections import deque

nums = list(map(int, input().split()))

def get_clock(n):
    q = deque(n)

    value = int(''.join(map(str, q)))

    for i in range(1, 4):
        q.rotate(1)
        now = int(''.join(map(str, q)))
        value = min(value, now)
    return value

clk_num = get_clock(nums)
cnt = 1

for i in range(1111, clk_num):
    if '0' not in list(str(i)) and i == get_clock(list(map(int, str(i)))):
        cnt += 1

print(cnt)

