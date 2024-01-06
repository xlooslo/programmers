"""
다음번에 들어갈 트럭의 무게가 다리의 한계량보다 높을 경우 무게가 0인 트럭을 다리에 추가하는 것이 가장 핵심 아이디어.
트럭마다 현재 남은 시간을 계산하는 방법도 있겠으나 for문을 매번 돌려야 해서 비효율적임.
"""

def solution(length, w_limit, trucks):
    w = 0
    time = 0
    bridge = [0] * length
    trucks = trucks[::-1]
    
    while trucks != []:
        time += 1
        
        if bridge:
            w -= bridge.pop(0)
        
        if w + trucks[-1] <= w_limit:
            tmp = trucks.pop() # 들어갈 트럭
            bridge.append(tmp) # bridge에 올라감
            w += tmp           # 현재 w에 추가
        else:
            bridge.append(0)   # 무게 0짜리 트럭 추가
    
    return time + length
