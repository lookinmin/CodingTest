def solution(numbers):
    answer = []

    # 짝수의 경우, 가장 뒤에 있는 0 -> 1
    # 홀수의 경우, 가장 뒤의 0의 위치를 idx라 할 때,
    # [idx] = 1 / [idx + 1] = 0
    # 0111 -> 1011

    for number in numbers:
        stand = list('0' + bin(number)[2:])
        idx = ''.join(stand).rfind('0')
        stand[idx] = '1'

        if number % 2 == 1:
            stand[idx + 1] = '0'

        answer.append(int(''.join(stand), 2))



    # 시간초과 10, 11 TC
    # for number in numbers:
    #     stand = bin(number)[2:]
    #     num = number
    #     while 1:
    #         res = 0
    #         num += 1
    #         tmp = bin(num)[2:]
    #         len_tmp = len(tmp)
    #         if len(stand) < len_tmp:
    #             k = len_tmp - len(stand)
    #             check = "0" * k + stand
    #         else:
    #             check = stand
    #
    #         for i in range(len_tmp):
    #             if tmp[i] != check[i]:
    #                 res += 1
    #         if res <= 2:
    #             answer.append(num)
    #             break
    return answer

print(solution([2, 7]))