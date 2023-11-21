def solution(survey, choices):
    answer = ''
    SG = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    # R vs T / C vs F / J vs M / A vs N

    for i in range(len(survey)):
        a = survey[i][0]
        b = survey[i][1]

        if choices[i] == 1:
            SG[a] += 3
        elif choices[i] == 2:
            SG[a] += 2
        elif choices[i] == 3:
            SG[a] += 1
        elif choices[i] == 5:
            SG[b] += 1
        elif choices[i] == 6:
            SG[b] += 2
        elif choices[i] == 7:
            SG[b] += 3

    if SG['R'] >= SG['T']:
        answer += 'R'
    else:
        answer += 'T'

    if SG['C'] >= SG['F']:
        answer += 'C'
    else:
        answer += 'F'

    if SG['J'] >= SG['M']:
        answer += 'J'
    else:
        answer += 'M'

    if SG['A'] >= SG['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer