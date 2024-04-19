# 7 더하기, S3
from sys import stdin

code = {
    "063": 0,
    "010": 1,
    "093": 2,
    "079": 3,
    "106": 4,
    "103": 5,
    "119": 6,
    "011": 7,
    "127": 8,
    "107": 9,
}

code_rev = {v : k for k, v in code.items()}

while 1:
    tc = stdin.readline().rstrip()
    if tc == 'BYE':
        break
    left = tc.split('+')[0]
    right = tc.split('+')[1][:-1]

    nums_left = ""
    nums_right = ""

    for i in range(0, len(left), 3):
        num = list(left[i : i + 3])
        tmp = ''
        for w in num:
            tmp += w
        nums_left+=str(code[tmp])

    for i in range(0, len(right), 3):
        num = list(right[i : i + 3])
        tmp = ''
        for w in num:
            tmp += w
        nums_right+=str(code[tmp])

    val = int(nums_left) + int(nums_right)
    val = str(val)
    res = ''
    for w in val:
        res += code_rev[int(w)]

    print("{}{}".format(tc, res))
