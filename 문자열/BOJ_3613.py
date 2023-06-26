# Java vs C++, S3, 문자열

from sys import stdin

# JAVA = 첫 단어는 소문자로 쓰고, 다음 단어부터는 첫 문자만 대문자로 쓴다. 또, 모든 단어는 붙여쓴다
# C++ = 변수명에 소문자만 사용한다. 단어와 단어를 구분하기 위해서 밑줄('_')을 이용한다.

origin = stdin.readline().rstrip()
error = "Error!"
if '_' in origin:       # C++ to JAVA
    if "__" in origin:
        print(error)
        exit(0)
    if origin[0] == '_' or origin[-1] =='_':
        print(error)
        exit(0)
    if not origin.islower():
        print(error)
        exit(0)
    arr=[]
    for word in origin.split('_'):
        if not arr:
            arr.append(word)
        else:
            arr.append(word.capitalize())       # 첫 단어만 대문자로 바꿔서 넣기


    # for i in range(len(origin)):      # 런타임 에러, 내가 돌리면 괜찮았음
    #     if origin[i] == '_':
    #         origin[i+1] = origin[i+1].upper()
    # remove = {'_'}
    # arr = [i for i in origin if i not in remove]

    print(''.join(arr))
else:
    arr=[]
    for i in range(len(origin)):
        if origin[i].isupper():
            if i == 0:
                print(error)
                exit(0)
            else:
                arr.append('_' + origin[i].lower())
        else:
            arr.append(origin[i].lower())
        # if 'A' <= origin[i] <= 'Z':
        #     origin[i] = '_'+origin[i].lower()
    print(''.join(arr))
