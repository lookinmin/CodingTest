import sys

T = int(sys.stdin.readline())
pad = {'0': [1, 1, 1, 1, 0, 1, 1],
       '1': [0, 0, 1, 0, 0, 1, 0],
       '2': [0, 1, 1, 1, 1, 0, 1],
       '3': [0, 1, 1, 0, 1, 1, 1],
       '4': [1, 0, 1, 0, 1, 1, 0],
       '5': [1, 1, 0, 0, 1, 1, 1],
       '6': [1, 1, 0, 1, 1, 1, 1],
       '7': [1, 1, 1, 0, 0, 1, 0],
       '8': [1, 1, 1, 1, 1, 1, 1],
       '9': [1, 1, 1, 0, 1, 1, 1]}

for _ in range(T):
    A, B = sys.stdin.readline().split()
    padA, padB = [[0] * 7 for _ in range(5)], [[0] * 7 for _ in range(5)]
    for w in A:
        padA.append(pad[w])
    padA = padA[-5:]
    for w in B:
        padB.append(pad[w])
    padB = padB[-5:]
    cnt = 0
    for i in range(5):
        for j in range(7):
            if padA[i][j] != padB[i][j]:
                cnt += 1
    print(cnt)