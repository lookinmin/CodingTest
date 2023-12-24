# 시간초과
# 백만 * 백만은 에바긴 함

def solution(numbers):
    answer = []

    for idx in range(len(numbers) - 1):
        tmp = numbers[idx + 1:]
        flag = False
        for i in range(len(tmp)):
            if tmp[i] > numbers[idx]:
                answer.append(tmp[i])
                flag = True
                break
        if flag == False:
            answer.append(-1)
    answer.append(-1)

    return answer

# 스택을 통한 풀이
# 인덱스를 스택에 넣는다...
# LV2 치곤 좀 어렵지 않았나

def solution(numbers):
    answer = [-1] * len(numbers)

    stack = []  # 인덱스가 담긴다

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)  # 인덱스를 넣는다
    return answer