from itertools import combinations

def solution(orders, course):
    answer = []

    for num in course:
        dic = {}
        
        for i in range(len(orders)):
            canMake = list(combinations(sorted(orders[i]), num))
            all_str = []  # 만들수 있는 모든 문자열
            for k in range(len(canMake)):
                tmp = ''
                for j in range(num):

                    tmp += canMake[k][j]
                if tmp in dic:
                    dic[tmp] += 1
                else:
                    dic[tmp] = 1

        if len(dic) > 0:
            maxVal = max(list(dic.values()))
            tk = []
            for i in dic.keys():
                if dic[i] == maxVal and maxVal >= 2:
                    tk.append(i)
            for i in tk:
                answer.append(i)
        else:
            continue


    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))