def solution(routes):
    answer = 0

    routes.sort(key= lambda x : x[1])
    camera = []
    camera.append(routes[0][1])

    for route in routes:
        start = route[0]
        end = route[1]
        if camera[-1] < start:
            camera.append(end)

    answer = len(camera)


    return answer

# --------------------------

def solution(routes):
    routes.sort(key = lambda x : x[1])    
    cnt = 0
    last_pos = -30001
    
    for route in routes:
        s, e = route
        
        if last_pos < s:
            cnt+=1
            last_pos = e
    
    return cnt
    