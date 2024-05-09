# 진짜 메시지, S4
from sys import stdin
n = int(stdin.readline())
for _ in range(n):
    message = stdin.readline().rstrip()
    flag = False

    msg = [0 for _ in range(26)]    # 총 알파벳 수
    res = 'OK'
    for i in range(len(message)):
        idx = ord(message[i]) - 65
        if flag:
            flag = False
            continue
        msg[idx] += 1
        if msg[idx] == 3:
            if i == len(message) - 1:
                # 뒤에 똑같은게 하나 더 있어야 함
                res = 'FAKE'
                break
            elif message[i] != message[i + 1]:
                res = 'FAKE'
                break
            flag = True
            msg[idx] = 0
    print(res)