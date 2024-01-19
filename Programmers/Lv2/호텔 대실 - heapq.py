import heapq

def solution(book_time):
    answer = 1
    arr = []
    for start, end in book_time:
        sh, sm = start.split(':')
        sh = int(sh) * 60
        sm = int(sm)
        eh, em = end.split(':')
        eh = int(eh) * 60
        em = int(em)
        arr.append([sh + sm, eh + em + 10])

    rooms = []

    for s, e in sorted(arr):
        if not rooms:
            heapq.heappush(rooms, e)
            continue
        if rooms[0] <= s:
            heapq.heappop(rooms)
        else:
            answer += 1
        heapq.heappush(rooms, e)
    return answer