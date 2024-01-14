def solution(weights):
    answer = 0
    dict = {}

    for weight in weights:
        dict[weight] = dict.get(weight, 0) + 1

    for key, value in dict.items():
        if value > 1:
            answer += value * (value - 1) // 2
            # 같은 무게의 원소가 2개 이상일 때, 무작위로 2개 뽑기 (nC2)
        if key * 2 in dict:
            # 현재 체크 원소 무게의 2배가 weights 안에 있다
            answer += value * dict[key * 2]
            # 해당 무게의 elements의 수만큼
        if key * 3 % 2 == 0 and key * 3 // 2 in dict:
            answer += value * dict[key * 3 // 2]
        if key * 4 % 3 == 0 and key * 4 // 3 in dict:
            answer += value * dict[key * 4 // 3]

    return answer