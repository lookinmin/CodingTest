# 거듭제곱, S4, 비트마스킹

n = int(input())

# 10진수 N → 2진수 → 3진법 → 10진수
# ex) 7번째 수 = 7 → bin(7) = 111 → 9 + 3 + 1 → 13

v = list(bin(n)[2:][::-1])      #0b111 → 0b날리기

t = 1
res = 0

for bit in v:
    res += int(bit) * t
    t *= 3

print(res)