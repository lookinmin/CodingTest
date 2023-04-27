# 신기한 소수, G5, 수학-백트래킹
import math

n = int(input())
# n은 자릿수

def isPrime(x): # 소수인지 판별해주는 함수
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:      # 요구 자릿수 도달
        print(num)
    else:
        for i in range(10):
            tmp = num * 10 + i  # 해당 수 부터 자릿 수 늘린 수가 소수 ex) 21, 22, 23 ...
            if isPrime(tmp):
                dfs(tmp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)      # 한자리 수 중 소수인 수들로 dfs 시작


        # 시간 초과
# if n == 1:
#     for i in range(1, 10):
#         if isPrime(i):
#             res.append(i)
# elif n == 2:        # 두자리수
#     for i in range(10, 100):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(i):
#             res.append(i)
# elif n == 3:
#     for i in range(100, 1000):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(int(num[0]+num[1])) and isPrime(i):
#             res.append(i)
# elif n == 4:
#     for i in range(1000, 10000):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(int(num[0]+num[1])) and isPrime(int(num[0]+num[1]+num[2])) and isPrime(i):
#             res.append(i)
# elif n == 5:
#     for i in range(10000, 100000):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(int(num[0] + num[1])) and isPrime(
#                 int(num[0] + num[1] + num[2])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3])) and isPrime(i):
#             res.append(i)
# elif n == 6:
#     for i in range(100000, 1000000):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(int(num[0] + num[1])) and isPrime(
#                 int(num[0] + num[1] + num[2])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3] + num[4])) and isPrime(i):
#             res.append(i)
# elif n == 7:
#     for i in range(1000000, 10000000):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(int(num[0] + num[1])) and isPrime(
#                 int(num[0] + num[1] + num[2])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3] + num[4])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3] + num[4] + num[5])) and isPrime(i):
#             res.append(i)
# else:
#     for i in range(10000000, 100000000):
#         num = str(i)
#         if isPrime(int(num[0])) and isPrime(int(num[0] + num[1])) and isPrime(
#                 int(num[0] + num[1] + num[2])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3] + num[4])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3] + num[4] + num[5])) and isPrime(
#                 int(num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6])) and isPrime(i):
#             res.append(i)