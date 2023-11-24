import sys
sys.setrecursionlimit(10 ** 8)

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [0] * len(words)

    ans = []

    def dfs(current, cnt, visited):
        global ans
        if current == target:
            ans.append(cnt)
            return

        for i in range(len(words)):
            if visited[i] == 0:
                tmp = 0
                for j in range(len(words[i])):
                    if words[i][j] != current[j]:
                        tmp += 1

                if tmp == 1:
                    visited[i] = 1
                    dfs(words[i], cnt + 1, visited)
                    visited[i] = 0

    dfs(begin, 0, visited)
    answer = min(ans)
    return answer



# 1. bfs
from collections import deque

def solution(begin, target, words):
    answer = 0

    q = deque()
    q.append([begin, 0])
    visited = [0 for _ in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            dist = 0
            if visited[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        dist += 1

                if dist == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = 1

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))