# S1, 나무꾼 이다솜
from sys import stdin

# 나무 길이 동일 조정
# 나무 자를때 C원
# 한 단위당 W원
# K * L * W

n, c, w = map(int, stdin.readline().split())
trees = []

for _ in range(n):
    trees.append(int(stdin.readline().rstrip()))

max_length = max(trees)


res = -float('inf')
for length in range(1, max_length + 1):
    total_profit = 0
    for i in range(n):
        if trees[i] < length:
            continue
        
        pieces = trees[i] // length
        cut = pieces - 1 if trees[i] % length == 0 else pieces
        
        profit = (pieces * length * w) - (cut * c)
        if profit > 0:
            total_profit += profit
    res = max(res, total_profit)
print(res)