def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    while people:
        tmp = limit - people[0]
        if len(people) >= 2 and tmp >= people[-1]:
            del people[0]
            people.pop()
        else:
            del people[0]

        answer += 1

    return answer

# 테스트 케이스는 통과했으나 효율성 테스트에서 실패함

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        answer += 1

    if people:
        answer += 1
    return answer

# deque를 통한 개선으로 통과

def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people) - 1

    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1  # 2명씩 태워보낼 수 있는 보트의 수를 센다
        end -= 1  # 2명씩 못탄다면, 제일 무거운 사람이 혼자 타고 간 것
    answer = len(people) - answer  # 한번에 한명씩 보낸 횟수에서 두명씩 타고 간 횟수를 뺀게 답

    return answer

# 투 포인터를 통한 시간 복잡도 개선