# 막대기, S5, 비트마스킹
# 입력값을 2진수로 변환했을 때, 1의 개수 찾기

x = int(input())
# 비트 수 64까지
res = 0

x = bin(x)
for bit in x:
    if bit == '1':
        res += 1

print(res)

# 구현으로 풀기
stick = 64
cnt = 0

while x != 0:
    if x >= stick:
        cnt += 1
        x -= stick
    else:
        stick //= 2

print(cnt)