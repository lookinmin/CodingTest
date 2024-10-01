def solution(s):
    answer = []
    
    for x in s:
        # 1,000,000 이기 때문에 permutation (X)
        stack = []
        cnt_110 = 0
        idx = 0
        
        while idx < len(x):
            if x[idx] == '0':
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop()
                    cnt_110 += 1
                    idx += 1
                else:
                    stack.append(x[idx])
                    idx += 1
            else:
                stack.append(x[idx])
                idx += 1
        
        stack = ''.join(stack[::-1])
        idx = stack.find('0')
        # 0이 처음 나타나는 위치
        
        if idx != -1:
            res = stack[:idx] + '011' * cnt_110 + stack[idx:]
        else:   # 없으면 맨앞에
            res = stack + '011' * cnt_110
        
        answer.append(''.join(res[::-1]))
    return answer