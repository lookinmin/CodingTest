def solution(a, b):
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # date[1] = 금요일
    total = 0
    total += sum(day[:a-1])
    total += b
    index = date[total % 7]
    return index
