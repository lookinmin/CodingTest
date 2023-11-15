def solution(numbers, hand):
    answer = ''
    key = [[0] * 3 for _ in range(4)]
    # 1은 왼손, 2는 오른손
    key[3][0] = 1
    key[3][2] = 2

    prev_x1 = 3
    prev_y1 = 0

    prev_x2 = 3
    prev_y2 = 2

    for num in numbers:
        if num == 1:
            answer += 'L'
            key[0][0] = 1
            key[prev_x1][prev_y1] = 0
            prev_x1, prev_y1 = 0, 0
        elif num == 4:
            answer += 'L'
            key[1][0] = 1
            key[prev_x1][prev_y1] = 0
            prev_x1, prev_y1 = 1, 0
        elif num == 7:
            answer += 'L'
            key[2][0] = 1
            key[prev_x1][prev_y1] = 0
            prev_x1, prev_y1 = 2, 0
        elif num == 3:
            answer += 'R'
            key[0][2] = 2
            key[prev_x2][prev_y2] = 0
            prev_x2, prev_y2 = 0, 2
        elif num == 6:
            answer += 'R'
            key[1][2] = 2
            key[prev_x2][prev_y2] = 0
            prev_x2, prev_y2 = 1, 2
        elif num == 9:
            answer += 'R'
            key[2][2] = 2
            key[prev_x2][prev_y2] = 0
            prev_x2, prev_y2 = 2, 2
        elif num == 2:
            dist1 = abs(0 - prev_x1) + abs(1 - prev_y1)
            dist2 = abs(0 - prev_x2) + abs(1 - prev_y2)
            if dist1 < dist2:
                answer += 'L'
                key[0][1] = 1
                key[prev_x1][prev_y1] = 0
                prev_x1, prev_y1 = 0, 1
            elif dist1 > dist2:
                answer += 'R'
                key[0][1] = 2
                key[prev_x2][prev_y2] = 0
                prev_x2, prev_y2 = 0, 1
            else:
                if hand == 'left':
                    answer += 'L'
                    key[0][1] = 1
                    key[prev_x1][prev_y1] = 0
                    prev_x1, prev_y1 = 0, 1
                else:
                    answer += 'R'
                    key[0][1] = 2
                    key[prev_x2][prev_y2] = 0
                    prev_x2, prev_y2 = 0, 1
        elif num == 5:
            dist1 = abs(1 - prev_x1) + abs(1 - prev_y1)
            dist2 = abs(1 - prev_x2) + abs(1 - prev_y2)
            if dist1 < dist2:
                answer += 'L'
                key[1][1] = 1
                key[prev_x1][prev_y1] = 0
                prev_x1, prev_y1 = 1, 1
            elif dist1 > dist2:
                answer += 'R'
                key[1][1] = 2
                key[prev_x2][prev_y2] = 0
                prev_x2, prev_y2 = 1, 1
            else:
                if hand == 'left':
                    answer += 'L'
                    key[1][1] = 1
                    key[prev_x1][prev_y1] = 0
                    prev_x1, prev_y1 = 1, 1
                else:
                    answer += 'R'
                    key[1][1] = 2
                    key[prev_x2][prev_y2] = 0
                    prev_x2, prev_y2 = 1, 1
        elif num == 8:
            dist1 = abs(2 - prev_x1) + abs(1 - prev_y1)
            dist2 = abs(2 - prev_x2) + abs(1 - prev_y2)
            if dist1 < dist2:
                answer += 'L'
                key[2][1] = 1
                key[prev_x1][prev_y1] = 0
                prev_x1, prev_y1 = 2, 1
            elif dist1 > dist2:
                answer += 'R'
                key[2][1] = 2
                key[prev_x2][prev_y2] = 0
                prev_x2, prev_y2 = 2, 1
            else:
                if hand == 'left':
                    answer += 'L'
                    key[2][1] = 1
                    key[prev_x1][prev_y1] = 0
                    prev_x1, prev_y1 = 2, 1
                else:
                    answer += 'R'
                    key[2][1] = 2
                    key[prev_x2][prev_y2] = 0
                    prev_x2, prev_y2 = 2, 1
        elif num == 0:
            dist1 = abs(3 - prev_x1) + abs(1 - prev_y1)
            dist2 = abs(3 - prev_x2) + abs(1 - prev_y2)
            if dist1 < dist2:
                answer += 'L'
                key[3][1] = 1
                key[prev_x1][prev_y1] = 0
                prev_x1, prev_y1 = 3, 1
            elif dist1 > dist2:
                answer += 'R'
                key[3][1] = 2
                key[prev_x2][prev_y2] = 0
                prev_x2, prev_y2 = 3, 1
            else:
                if hand == 'left':
                    answer += 'L'
                    key[3][1] = 1
                    key[prev_x1][prev_y1] = 0
                    prev_x1, prev_y1 = 3, 1
                else:
                    answer += 'R'
                    key[3][1] = 2
                    key[prev_x2][prev_y2] = 0
                    prev_x2, prev_y2 = 3, 1
    return answer