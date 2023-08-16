# 베르트랑 공준, S2, 수학

from sys import stdin
import math

# 자연수 n에 대해 n < ? <= 2n인 소수는 적어도 하나

def isPrime(x):     # 그냥 소수판정으로
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


arr = [False, False] + [True]*(2*123456+1)
prime = []
def era(x):             # 에라토스테네스의 체로 풀기
    for i in range(2, x+1):
        if arr[i]:
            prime.append(i)

            for j in range(2*i, x+1, i):
                arr[j] = False


while 1:
    n = int(stdin.readline().rstrip())
    if n == 0:
        break

    cnt = 0

    era(2*123456)

    for i in range(n+1, 2*n+1):
        # if isPrime(i):
        #     cnt += 1
        if arr[i]:
            cnt += 1

    print(cnt)
