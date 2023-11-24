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

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))