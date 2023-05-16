# 펠린드롬 만들기, S2, 문자열

from sys import stdin

s = stdin.readline().rstrip()


# 부분 문자열이 펠린드롬이 되기까지의 왼쪽 문자열의 수 만큼 더해줌
# abbcd인 경우
# abbcd
# bbcd
# bcd
# cd
# d (d하나는 팰린드롬)
# 이렇게 검사해나가서 펠린드롬이 아니었던 abbc를 뒤집어서 d오른쪽에 cbba이렇게 붙인

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:        # 부분 문자열이 펠린드롬인 경우
        print(len(s) + i)
        break