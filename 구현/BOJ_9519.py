# 졸려, G5, 구현-문자열
# 단어의 뒷 부분 절반이 앞 부분과 섞이게 된다.
# 마지막 글자가 첫 번째 글자와 두 번째 글자 사이로 이동한다.
# 뒤에서 두 번째 글자가 두 번째 글자와 세 번째 글자 사이로 이동한다.
# 뒤에서 k번째 글자는 앞에서부터 k번째와 k+1번째 글자 사이로 이동한다.
from sys import stdin

x = int(stdin.readline())
word = stdin.readline().rstrip()
origin = word
word_list = [word]      # 변하는 문자들이 들어올 배열, 0번째 인덱스는 입력받은 문자

def solve():
    global x
    cnt = 0
    while 1:
        cnt += 1
        mix_word()          # 문자넣고
        if origin == word:      # 처음 입력한 문자와 규칙을 따라 돌다가 다시 같아졌다면 while문 중단
            break
        word_list.append(word)      # 생성된 문자열을 배열에 입력
    print(word_list[-x % len(word_list)])       # 0번째에서 -x 번째가 x번 깜박인 문자


def mix_word():
    global word, word_list
    tmp = ''
    for i in range(len(word) // 2):
        tmp += word[i] + word[len(word)-1-i]        # 규칙을 따라 지금 문자열에서 변형 시작

    if len(word)%2 != 0:
        tmp += word[len(word)//2]                   # 길이가 홀수라면 해당 문자열에 가운데 문자를 뒤에 넣어줘야함
    word = tmp      # 넣을 문자 생성

solve()