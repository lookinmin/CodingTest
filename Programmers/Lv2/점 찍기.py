def solution(k, d):
    answer = 0
    # 피타고라스 정리 -> y^2 = r^2 - x^2
    for x in range(0, d + 1, k):
        # x = 찍을 수 있는 점
        y = int((d**2 - x**2)**0.5)
        answer += (y // k) + 1
    return answer자