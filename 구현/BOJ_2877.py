# 4와 7, G5, 구현

K = int(input())
# 4외 7로만 이루어진 수들 중 K 번째로 작은 수 찾기
# K가 10^9까지, 시간제한 1초, permutation은 반드시 시간제한

from itertools import permutations

# k = 1이면, 4, k=2이면, 7
# 4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777 ...
# 2진수 / 4=0, 7=1

s = format(K+1, 'b')
s = s[1:]
print(s.replace('0', '4').replace('1', '7'))
