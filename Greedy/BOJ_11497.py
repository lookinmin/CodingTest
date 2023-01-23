# 통나무 건너뛰기, S1, 그리디 - 정렬
# 증가하다 감소하는 배열 만들기
from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    trees = list(map(int, stdin.readline().split()))
    tmp = []
    trees.sort()
    for i in range(1, len(trees)):
        if i % 2 != 0:
            tmp.append(trees[i])
    for i in tmp:
        if i in trees:
            trees.remove(i)
    for i in reversed(tmp):
        trees.append(i)
    res = []
    for i in range(1, len(trees)):
        res.append(abs(trees[i] - trees[i-1]))
    res.append(abs(trees[len(trees)-1] - trees[0]))
    print(max(res))
