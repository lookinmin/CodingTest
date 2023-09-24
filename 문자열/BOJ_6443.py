# 애너그램, G5, 문자열

from sys import stdin
from itertools import permutations

def dfs(depth):
    if depth == len(word):
        print(''.join(res))
        return

    for v in visited:
        if visited[v]:
            visited[v] -= 1     # 해당 단어(v) res에 append
            res.append(v)
            dfs(depth + 1)      # 다음 단어 탐색
            visited[v] += 1     # 다시 초기화(사용 전)
            res.pop()           # 초기화를 위해 res에서 단어(v) 빼줌


n = int(stdin.readline())
for _ in range(n):
    word = sorted(list(map(str, stdin.readline().rstrip())))
    visited = {}
    res = []

    for w in word:
        if w in visited:
            visited[w] += 1
        else:
            visited[w] = 1

    dfs(0)


    # permutation 쓰면 답은 나오는데 메모리초과 걸림
    # tmp = list(set(list(permutations(word, len(word)))))
    #
    # tmp.sort()
    # for w in tmp:
    #     for i in w:
    #         print(''.join(i),end="")
    #     print()

