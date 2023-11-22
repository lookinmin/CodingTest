from collections import deque


def solution(cacheSize, cities):
    answer = 0
    buffer = deque(maxlen=cacheSize)

    if cacheSize == 0:
        return len(cities) * 5
    else:
        # 1. city in buffer +1
        # 2. no, remove -> append
        for city in cities:
            city = city.lower()
            if city in buffer:
                answer += 1
                buffer.remove(city)
            else:
                answer += 5
            buffer.append(city)
    return answer

