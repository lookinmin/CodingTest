# 오리, S3, 문자열

from sys import stdin

sound = stdin.readline().rstrip()
quack = 'quack'
visited = [0] * len(sound)

cnt = 0
def find(start):
    global cnt
    idx = 0
    first = 1

    for i in range(start, len(sound)):
        if sound[i] == quack[idx] and not visited[i]:
            visited[i] = 1
            if sound[i] == 'k':
                if first:
                    cnt += 1
                    # 오리가 연속으로 돌면 하나만 카운트
                    first = 0
                idx = 0         # k까지 나왔으면 다시 q부터 찾기
            else:
                idx += 1        # q -> u, 다음 문자 비교

if len(sound) % 5 != 0:
    print(-1)
    exit()

for i in range(len(sound)):
    if sound[i] == 'q' and not visited[i]:
        find(i)

if cnt == 0 or not all(visited):        # 오리 수 0마리, 전부 방문하지 않았음
    print(-1)
else:
    print(cnt)
