from sys import stdin

n = int(input())  # 체인의 개수 N 입력
arr = list(map(int, stdin.readline().split()))  # 체인의 길이 배열 입력
arr.sort()  # 체인의 길이를 오름차순으로 정렬

use = 0  # 사용된 고리의 개수를 누적하는 변수

for num in arr:
    if n <= 1:  # 남은 체인이 1개 이하라면 더 이상 연결할 필요 없음
        print(use)
        exit(0)

    if num == n - 1:  # 현재 체인의 길이가 남은 체인 수(n - 1)와 같은 경우
        print(use + num)  # 필요한 고리 수 출력
        exit(0)

    elif num > n - 1:  # 현재 체인의 길이가 남은 체인 수보다 크면 더 이상 연결할 수 없으므로
        print(use + n - 1)  # 남은 체인 수만큼 고리를 열고 닫음
        exit(0)

    else:  # 현재 체인의 길이가 n-1보다 작은 경우
        n -= (num + 1)  # 현재 체인을 하나의 연결 고리로 줄였다고 가정하고 체인의 개수 감소
        use += num  # 현재 체인에서 사용된 고리 수 누적

print(0)
