def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def Quad(a, b, length):
        start = arr[a][b]
        # 시작값 확인
        for i in range(a, a + length):
            for j in range(b, b + length):
                if arr[i][j] != start:  # 다른 수 있으면 재귀적으로
                    length //= 2
                    Quad(a, b, length)
                    Quad(a, b + length, length)
                    Quad(a + length, b, length)
                    Quad(a + length, b + length, length)
                    return
                # 다른 수 없으면 재귀 끝, 해당 tmp 배열의 시작 수 인덱스 증가
        answer[start] += 1

    Quad(0, 0, n)

    return answer