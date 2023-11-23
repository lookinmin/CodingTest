import math

def solution(fees, records):
    answer = []
    # fees[0] : 기본 시간 / fees[1] : 기본 요금 / fees[2] : 단위 시간 / fees[3] : 단위 요금

    parking = {}
    stack = []
    for record in records:
        tmp = record.split(' ')
        time = tmp[0].split(':')
        minutes = int(time[0])*60 + int(time[1])
        if tmp[2] == 'IN':
            if tmp[1] in parking:
                parking[tmp[1]].append(minutes)
            else:
                parking[tmp[1]] = [minutes]
            stack.append(tmp[1])

        if tmp[2] == 'OUT':
            prev_time = parking[tmp[1]][-1]
            parking[tmp[1]].pop()
            parking[tmp[1]].append(minutes - prev_time)
            stack.remove(tmp[1])


    maxM = 23*60 + 59

    if stack:
        for num in stack:
            prev_time = parking[num][-1]
            parking[num].pop()
            parking[num].append(maxM -prev_time)


    res = {}
    for i in range(len(parking.keys())):
        tmp = list(parking.keys())[i]
        time = sum(parking[tmp])
        money = 0
        if time > fees[0]:
            money += fees[1]
            # time -= fees[0]

            money += (math.ceil(max(0, (time-fees[0])) / fees[2]) * fees[3])
            res[tmp] = money
        else:
            money = fees[1]
            res[tmp] = money

    k = sorted(res.items())

    for i in k:
        answer.append(i[1])

    return answer


print(solution([180, 5000, 10, 1000],["05:59 0000 IN", "05:59 1111 IN"] ))


