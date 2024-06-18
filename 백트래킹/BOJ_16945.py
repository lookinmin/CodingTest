# 매직스퀘어로 변경
from sys import stdin
board = [[0] * 3 for _ in range(3)]
for i in range(3):
    board[i] = list(map(int, stdin.readline().split()))

res = int(1e9)

def dfs(depth):
