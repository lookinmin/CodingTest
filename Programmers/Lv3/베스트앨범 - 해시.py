def solution(genres, plays):
    answer = []
    dict = {}
    for i in range(len(genres)):
        dict[i] = [genres[i], plays[i]]

    genre_dict = {}
    for genre in dict.values():
        genre_dict[genre[0]] = genre_dict.get(genre[0], 0) + genre[1]

    # 1. 속한 노래가 많이 재생된 장르 먼저
    tmp = sorted(genre_dict.items(), reverse=True, key=lambda x: x[1])
    # 2. 장르 내에서 많이 재생된 노래 먼저
    tmp2 = sorted(dict.items(), reverse=True, key=lambda x: (x[1][1], -x[0]))  # value의 두번째 값 = 재생 횟수
    # 3. 재생횟수가 같으면 idx가 낮을 수록 먼저

    check = {}

    for genre in tmp:
        now = genre[0]
        check[now] = 0
        for song in tmp2:
            if song[1][0] == now:
                if check[song[1][0]] < 2:
                    answer.append(song[0])
                    check[song[1][0]] += 1
    return answer