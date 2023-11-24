answer = [-1, -1]
def solution(users, emoticons):
    disRate = [10, 20, 30, 40]
    n, m = len(users), len(emoticons)

    dis_list = [0] * m

    def search(idx):
        global answer

        if idx == m:
            join, cost = 0, 0

            for rate, price in users:
                tmp = 0
                for j in range(m):
                    if rate <= dis_list[j]:
                        tmp += emoticons[j] * (100 - dis_list[j]) // 100

                if tmp >= price:
                    join += 1
                else:
                    cost += tmp
            if join > answer[0] or join == answer[0] and cost > answer[1]:
                answer = [join, cost]
            return
        for i in range(4):
            dis_list[idx] = disRate[i]
            search(idx + 1)     # dfs식 재귀

    search(0)
    # 할인은 10/20/30/40 중 1개
    # 이모티콘마다 할인율 다름
    # 가입자수 > 판매액
    return answer

print(solution([[40, 10000], [25, 10000]], 	[7000, 9000]))