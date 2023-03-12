# 단축키 지정, S1, 구현
# 각 단어의 첫 글자가 우선
from sys import stdin

T = int(stdin.readline())

shortcut = []
res = []
for _ in range(T):
    word = list(map(str, stdin.readline().split()))

    for i in range(len(word)):                  # 각 단어의 첫 알파벳부터 확인
        if word[i][0].upper() not in shortcut:
            shortcut.append(word[i][0].upper())
            word[i] = "[" + word[i][0] + "]" + word[i][1:]
              # 현재 단어를 []로 감싸기
            print(*word)
            break
    else:           # 반복문이 break를 통과하지 않았음
        for j in range(len(word)):              # 각 단어의 왼쪽알파벳부터 차례대로 확인
            flag = False        # 현재 단어의 알파벳을 단축키로 사용했는지에 대한  flag
            for k in range(1, len(word[j])):
                if word[j][k].upper() not in shortcut:
                    shortcut.append(word[j][k].upper())
                    flag = True
                    word[j] = word[j][:k] + "[" + word[j][k] + "]" + word[j][k + 1:]
                    print(*word)
                    break
            if flag:
                break
        else:
            print(*word)            # 해당 단어의 모든 알파벳이 단축키로 이미 지정되어있음
