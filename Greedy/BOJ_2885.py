# 초콜릿 식사, S2, 그리디

k = int(input())

choco = 1

while 1:
    if choco >= k:
        break
    choco *= 2
val = choco
res = 0

while 1:
    if k % choco == 0:
        break
    else:
        choco //= 2
        res += 1

print(val, res)


