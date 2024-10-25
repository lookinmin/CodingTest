# 피자 오븐, G5
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    btns = [0] * 5
    sixties = n // 60
    # 현재 n 값이 60 이상일때, 60을 무조건 누르는게 맞다
    tens = (n % 60) // 10
    # n이 60 이하, 59라면, tens 는 5
    ones = n % 10
    # n의 일의자리수
    
    if ones > 5:
        # 일의 자리 수가 5 초과
        tens += 1
        ones -= 10
        # 10 에서 내려오는게 이득
    
    if tens > 3:
        # 십의 자리수가 3 초과
        sixties += 1
        tens -= 6
        # 60에서 내려오는게 이득
    
    if tens < 0 and ones == 5:
        # 60분 단위 올리는 과정에서 tens가 음수임
        # 그리고 정확히 일의 자리수가 5
        tens += 1
        ones -= 10
        
    btns[0] = sixties
    btns[2 - (tens >= 0)] = abs(tens)
    btns[4 - (ones >= 0)] = abs(ones)
    
    print(*btns)