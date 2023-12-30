def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        cnt = 0  # 약수의 개수

        for i in range(1, int((num) ** 0.5) + 1):
            if num % i == 0:
                cnt += 1
                if i ** 2 != num:
                    cnt += 1

        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer