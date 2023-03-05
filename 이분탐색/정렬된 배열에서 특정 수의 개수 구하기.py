# n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
# x가 등장하는 횟수는?


from bisect import bisect_left, bisect_right
from sys import stdin

N, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

a = bisect_right(arr, x)
b = bisect_left(arr, x)

print(a-b)