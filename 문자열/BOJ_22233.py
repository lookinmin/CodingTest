# 가희와 키워드, S2, 문자열

from sys import stdin

# 키워드 최대 10개, 메모장에 있던거 -> 작성하면 지워짐

n, m = map(int, stdin.readline().split())
keyword=dict()
for _ in range(n):
    tmp = stdin.readline().rstrip()
    keyword[tmp] = 1

res = n

for _ in range(m):
    write = sorted(stdin.readline().rstrip().split(','))
    # 시간초과, N, M의 크기가 너무 커서 in으로 다 돌면 초과임
    for word in write:
        if word in keyword.keys():      # 딕셔너리를 통해 탐색하면 시간초과가 나지 않음
            if keyword[word] == 1:
                keyword[word] -= 1
                res -= 1

    print(res)