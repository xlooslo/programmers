# Queue로 구현했으나 효율성 테스트에서 실패했습니다.
from collections import deque

def solution(scv, K):
    answer = 0
    scv.sort()
    cnt = len(scv)
    scv = deque(scv)

    while True:
        if scv[0] >= K:
            break
            
        if cnt == 1:
            answer = -1
            break
        
        scv[1] = scv[0] + scv[1] * 2
        scv.popleft()
        
        scv_sort(scv)
            
        answer += 1
        cnt -= 1
        
    return answer


def scv_sort(scv):
    for i in range(1, len(scv)):
        if scv[i-1] > scv[i]:
            scv[i-1], scv[i] = scv[i], scv[i-1]
    return
