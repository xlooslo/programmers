import heapq as hp

def solution(scv, K):
    answer = 0
    cnt = len(scv)
    scv.sort()
    hp.heapify(scv)

    while True:
        if scv[0] >= K:
            break
            
        if cnt == 1:
            answer = -1
            break
        
        min1 = hp.heappop(scv)
        min2 = min1 + hp.heappop(scv) * 2
        hp.heappush(scv, min2)
            
        answer += 1
        cnt -= 1
        
    return answer
