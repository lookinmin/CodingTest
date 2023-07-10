# 수학숙제, S4, 문자열
# 숫자 & 알파벳 소문자임

from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    tmp = list(stdin.readline().rstrip())
    num = ''
    for i in tmp:
        if 'a' <= i <= 'z':     # 값이 영어 소문자일때
            if num:             # num에 담아놓은 수가 있다면
                arr.append(int(num))        # 수를 arr에 넣고
                num = ''        # 수 초기화
            else:
                num = ''
        else:
            num += i            # 값이 숫자라면 수 만들기
    if num:     # 수가 들어있다면
        arr.append(int(num))

arr.sort()

for i in arr:
    print(i)

