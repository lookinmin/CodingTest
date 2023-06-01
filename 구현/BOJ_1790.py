# 수 이어쓰기2, G5, 구현

from sys import stdin

n, k = map(int, stdin.readline().split())

# for i in range(1, n+1):
#     nums += str(i)      # 무지성 문자열에 수 더하면 시간초과가 난다

# k가 1~9 = 한 자리수
# k가 10~99 = 두 자리수
# 원하는 자리수 k가 200이라면, 200을 넘지않는 선에서 1의 자리 수, 10의 자리수가 모두 사용 됨
# 1의 자리수 9개 + 90*2 = 189
# 200-189 = 11 이므로, 200까지 11칸 남음
# 이제 100의 자릿수만 남았으므로 (11-1) / 3의 몫, 나머지 계산
# 몫 = 3 -> 100의 자리수가 사용된 횟수

last_num = 0        # 마지막으로 사용된 수
num_len = 1         # 현재 자릿수
num_cnt = 9         # 현재 자릿수의 모든 숫자의 수(1~9)

while k > num_len * num_cnt:        # 남은 자리수 > 현재자리수 x 모든 수의 개수 보다 크다면
    k -= num_len * num_cnt      # 남은 자리수 업데이트
    last_num += num_cnt         # 마지막으로 사용된 수 증가
    num_len += 1                # 자릿수 증가
    num_cnt = num_cnt * 10      # 현재 자릿수의 모든 숫자의 개수 증가(한 자리일땐 9개, 두 자리일땐 90개)

last_num = (last_num + 1) + ((k-1)// num_len)

if last_num > n:
    print(-1)
else:
    print(str(last_num)[(k-1) % num_len])