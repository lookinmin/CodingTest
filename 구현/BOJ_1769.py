# 3의 배수, 구현 ,S5

x = input()
cnt = 0

def func(string, cnt):
    if len(string) > 1:
        cnt += 1
        tmp = 0
        for w in string:
            tmp += int(w)
        func(str(tmp), cnt)
    else:
        if int(string) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

func(x, cnt)