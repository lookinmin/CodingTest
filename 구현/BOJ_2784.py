# 가로 세로 퍼즐, S2
from sys import stdin

# 6개의 단어 입력 받기
words = [stdin.readline().strip() for _ in range(6)]

ans_list = []
for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == j or i == k or j == k:
                continue
            temp = [words[i], words[j], words[k]]
            temp2 = temp.copy()
            for h in range(3):
                temp2.append(temp[0][h] + temp[1][h] + temp[2][h])
            temp2.sort()
            if words == temp2:
                ans_list.append(temp[0] + temp[1] + temp[2])
ans_list.sort()
if len(ans_list):
    for i in range(0, 10, 3):
        print(ans_list[0][i:i + 3])
else:
    print(0)