# 생태학, S2, 문자열

from sys import stdin

trees = {}
cnt = 0

while 1:
    tree = stdin.readline().rstrip()
    if not tree:        # 입력이 들어오지 않으면 종료
        break

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    cnt += 1            # 총 갯수

arr = list(trees.keys())
arr.sort()

for i in arr:
    print("{} {:.4f}".format(i, trees[i]/cnt * 100))

