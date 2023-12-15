def solution(phone_book):
    answer = True
    book = sorted(phone_book, key=lambda x: (x, len(x)))

    for i in range(len(book) - 1):
        k = len(book[i])
        k2 = len(book[i+1])
        target = book[i]
        next = book[i+1]
        if k < k2:
            if target == next[:k]:
                return False

    return answer

#  효율성 3,4 실패 (아래)

def solution(phone_book):
    answer = True
    book = sorted(phone_book, key=lambda x: len(x))
    print(book)

    for i in range(len(book)):
        k = len(book[i])
        target = book[i]

        for j in range(i + 1, len(book)):
            tmp = book[j][:k]
            if target == tmp:
                return False

    return answer