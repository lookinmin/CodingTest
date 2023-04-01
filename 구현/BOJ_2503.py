# 숫자 야구, S3, 구현
# 세 자리 수에 있는 숫자들 중 하나가 영수의 세 자리 수의 동일한 자리에 위치하면 스트라이크 한 번
# 영수의 세 자리 수에 있긴 하나 다른 자리에 위치하면 볼 한 번

from sys import stdin
from itertools import permutations

ns = ['1','2','3','4','5','6','7','8','9']
numbers = list(permutations(ns, 3))         # 미리 가능한 모든 수의 조합을 만들어 놓고


n = int(stdin.readline())
res = []
for _ in range(n):
    a, s ,b = map(int, stdin.readline().split())

    num = list(str(a))
    cnt = 0
    for i in range(len(numbers)):               # 조합의 모든 수에 대해 탐색하면서
        strike, ball = 0, 0
        i -= cnt            # 조합에서 처음부터 다시 찾기 위해서
        for j in range(3):
            if numbers[i][j] == num[j]:         # 해당 위치의 수가 같으면
                strike += 1                     # 스트라이크
            elif num[j] in numbers[i]:          # 번호 있으면
                ball += 1                       # 볼


        if strike != s or ball != b:            # 현재 비교하는 수가
            numbers.remove(numbers[i])          # 주어진 s와 b까지 같지 않다면 조합에서 제거
            cnt += 1                            # i 인덱스를 0부터 시작 할 수 있도록

print(len(numbers))




