# 곱하기 혹은 더하기
# 그리디 예제, Facebook 인터뷰 출제
# 각 자리가 숫자인 문자열 S, 왼쪽부터 하나씩 모든 수를 확인하여 숫자 사이에 x 또는 +
# 만들어지는 가장 큰 수를 구함, 모든 연산은 왼쪽부터 순서대로

s = input()
res = int(s[0])
for i in range(1, len(s)):
    num = int(i)
    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num

print(res)

