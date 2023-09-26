# 기차가 어둠을 헤치고 은하수를, S2, 구현

from sys import stdin
# 기차 N개, 한 기차에 1~20까지
# 이미 같은 모양의 기차는 지나갈 수 없다
# 기차는 빈 상태로 시작

n, m = map(int, stdin.readline().split())

train = [[0] * 20 for _ in range(n+1)]
for _ in range(m):
    command = list(map(int, stdin.readline().split()))

    if command[0] == 1:
        train[command[1]][command[2]-1] = 1
    elif command[0] == 2:
        train[command[1]][command[2]-1] = 0
    elif command[0] == 3:
        train[command[1]] = [0] + train[command[1]][0:19]
    elif command[0] == 4:
        train[command[1]] = train[command[1]][1:20] + [0]

out = []
for i in range(1, n+1):
    if len(out) == 0:
        out.append(train[i])
    else:
        if train[i] in out:
            continue
        else:
            out.append(train[i])



print(len(out))