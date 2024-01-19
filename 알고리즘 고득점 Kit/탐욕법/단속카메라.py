# 나간 지점을 기준으로 오름차순으로 정렬 후
# 진입 지점보다 카메라의 위치가 더 크면 
# 무조건 중간에 카메라가 있음이 보장됨

def solution(routes):
    answer = 0
    cam = -30001
    
    routes.sort(key = lambda x:x[1])
    
    for car in routes:
        if car[0] > cam:
            answer += 1
            cam = car[1]
    
    return answer
