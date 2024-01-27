def solution(phone_number):
    tmp = phone_number[:-4]
    k = '*' * len(tmp)
    els = phone_number[-4:]
    return k + els
