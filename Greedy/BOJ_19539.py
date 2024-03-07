# 사과나무, G5, 그리디

from sys import stdin
n = int(stdin.readline())
trees = [0] * n
goal = list(map(int, stdin.readline().split()))
turn = sum(goal) // 3

if sum(goal) % 3 != 0:
    print("NO")
else:
    for tree in goal:
        turn -= (tree // 2)
    if turn > 0:
        print("NO")
    else:
        print("YES")