# 비밀번호 발음하기, S5, 문자열

from sys import stdin

# 모음 하나 반드시
# 모음3, 자음3 연속X
# ee, oo 제외 연속 단어 X

mo = ['a','e','i','o','u']
ok = ['ee', 'oo']

while 1:
    password = stdin.readline().rstrip()
    if password == 'end':
        break

    flag1 = False
    flag2 = True
    flag3 = True
    for i in range(len(password)):
        if password[i] in mo:
            flag1 = True

    for i in range(len(password) - 2):
        cnt = 0
        cnt2 = 0
        for w in password[i:i+3]:
            if w in mo:
                cnt += 1
            elif w not in mo:
                cnt2 += 1
        if cnt == 3 or cnt2 == 3:
            flag2 = False

    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            tmp = password[i] + password[i+1]
            if tmp not in ok:
                flag3 = False

    if flag1 and flag3 and flag2:
        print("<{}> is acceptable.".format(password))
    else:
        print("<{}> is not acceptable.".format(password ))