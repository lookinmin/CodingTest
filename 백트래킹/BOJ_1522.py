# 문자열 교환, G5, 완탐-슬라이딩 윈도우(크기가 정해진 투 포인터)

s = input().rstrip()

# 입력받은 s의 a의 갯수를 구해
# a개수 만큼의 구간을 만들어 한칸씩 이동
cnt_a = s.count('a')
res = int(1e9)
# a의 크기 만큼의 슬라이딩 윈도우에서 b의 갯수가 최소인 부분의 b의 갯수 찾기
for i in range(len(s)):
    tmp = ''
    if i + cnt_a >= len(s):     # 특정 부분이 s의 길이를 넘어갈 때
        comp = (i + cnt_a) % len(s)     # 해당 부분까지 합치기
        sub = s[i:len(s)] + s[0:comp]   # 현재 인덱스의 위치(i)부터 모든 a의 갯수 만큼 sub[]로 만들기
    else:
        sub = s[i:i+cnt_a]  # 현 인덱스 위치부터 a의 크기만큼의 슬라이딩 윈도우 만들기
    cnt_b = sub.count('b')  # 슬라이딩 윈도우 내의 b의 갯수 찾기
    res = min(res, cnt_b)   # 가장 적은 b의 갯수 만큼만 움직이면 됨

print(res)
