def solution(arr):
    answer = 0
    n = 1

    while 1:
        tmp = max(arr) * n
        flag = True
        for i in range(len(arr)):
            if tmp % arr[i] != 0:
                flag = False
                break
        if flag:
            break
        n += 1

    answer = tmp
    return answer

# 무식하게 풀어도 통과는 되더라

def solution(arr):
    from math import gcd                            # 최대공약수를 구하는 gcd() import
    answer = arr[0]                                 # answer을 arr[0]으로 초기화

    for num in arr:                                 # 반복문을 처음부터 끝까지 돈다.
        #1. (arr[0],arr[1])의 최소공배수를 구한 후 answer에 저장
        #2. (#1에서 구한 최소공배수, arr[2])의 최소공배수를 구한 후 answer에 저장
        #3. 모든 배열을 돌면서 최소공배수를 구하고, 저장하고 하는 방식을 진행
        answer = answer*num // gcd(answer, num)

    return answer