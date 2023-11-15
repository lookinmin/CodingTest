def solution(s):
    answer = []
    # 하나만 있으면 그게 a1
    # 두개 있으면 하나 있는거에 나머지 a2
    # 1. 문자열인 s를 리스트로 분류하기
    cut_s = s[2:-2]
    tmp = cut_s.split("},{")

    # 2. s의 부분을 s`라 할때, s`들을 len()순으로 정렬한다
    sorted_s = sorted(tmp, key=len)

    # 3. 각 s`내 원소들을 ',' 기준으로 나눠 answer에 없으면 넣는다.
    for w in sorted_s:
        k = w.split(',')
        for num in k:
            if int(num) not in answer:
                answer.append(int(num))
    return answer