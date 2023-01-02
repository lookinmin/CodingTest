# 구현-문자열, 문자열 재정렬
# 입력 : 문자열(알파벳 대문자 + 숫자)
# 출력 : 알파벳 오름차순 + 숫자더한값

a = input()
num = 0
res = []
for i in a:
    if i.isalpha():
        res.append(i)
    elif i.isdigit():
        num += int(i)

res.sort()
if num != 0:
    res.append(str(num))

print(''.join(res))