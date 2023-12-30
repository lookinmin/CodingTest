from collections import deque

def solution(bridge_length, weight, truck_weights):
    res = 0

    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    now = 0

    while len(truck_weights) > 0:
        res += 1
        now -= bridge.popleft()

        if now + truck_weights[0] <= weight:
            now += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    res += bridge_length
    return res