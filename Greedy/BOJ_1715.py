# 카드 정렬하기, G4, 그리디

from sys import stdin
import heapq

n = int(stdin.readline())
cards = []

for _ in range(n):
    card = int(stdin.readline().rstrip())
    cards.append(card)

heapq.heapify(cards)

res = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a + b
    res += c
    heapq.heappush(cards, c)

print(res)
