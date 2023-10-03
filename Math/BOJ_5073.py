# 삼각형과 세 변, B3, math

# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# Invalid : 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면

from sys import stdin

while 1:
    arr = list(map(int, stdin.readline().split()))
    if sum(arr) == 0:
        break
    arr.sort(reverse=True)
    if arr[0] >= arr[1] + arr[2]:
        print("Invalid")
    elif arr[0] == arr[1] == arr[2]:
        print("Equilateral")
    elif arr[0] != arr[1] != arr[2]:
        print("Scalene")
    else:
        print("Isosceles")