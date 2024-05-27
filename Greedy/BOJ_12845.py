# 모두의 마블, S3
from sys import stdin
n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))

res = 0
while len(cards) > 1:
    card = max(cards)
    idx = cards.index(card)
    left, right = int(1e9), int(1e9)
    if idx > 0:
        left = cards[idx - 1]
    if idx < len(cards) - 1:
        right = cards[idx - 1]

    if left > right:
        take = right
    else:
        take = left

    res += take + card
    cards.remove(take)

print(res)