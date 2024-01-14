def solution(n):
    answer = ''

    while n > 0:
        n, remain = divmod(n - 1, 3)
        # n-1을 3으로 나누어 몫과 나머지를 리턴
        # n이 아닌 n-1인 이유
        # 0, 1, 2가 아닌 1, 2, 4가 필요하기 때문에
        answer = '124'[remain] + answer
        # [1,2,4] 배열 중 해당하는 수를 가져옴
    return answer