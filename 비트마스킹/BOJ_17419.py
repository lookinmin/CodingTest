# 비트가 넘쳐흘러, S4, 비트마스킹
# 연산 K = K - (K&((~K) + 1))

from sys import stdin

n = int(stdin.readline())
k = stdin.readline().rstrip()       # 2진수가 들어옴
tmp = '0b' + k
num = int(tmp, 2)

cnt = 0
while num != 0:
    num = num - (num & ((~num) + 1))
    cnt += 1
print(cnt)

# 여기까지 51점

# 연산하면 제일 오른쪽 1이 0으로 바뀜
# 즉 1의 개수만큼 연산

print(k.count('1'))