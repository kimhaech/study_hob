# 무식하게 문제 그대로 풀기
# deque를 써서 현재 다리 위, 얼만큼 왔는지 기록, 남은 트럭, 도착한 트럭(얘는 안해도 무관하긴 함)
# 현재 다리 위 트럭 무게 합산을 매번 비교하면서 진행
# 다리 위에 트럭이 있는 경우 진행도 +1
from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque()
    on_bridge = deque()
    fin_bridge = deque()
    count_q = deque()
    time_count = 0
    
    for t in truck_weights: # 트럭들을 더하기
        trucks.append(t)
    
    while len(fin_bridge) < len(truck_weights): # 트럭이 다 지날 때 까지
        time_count += 1 # 시간 카운트

        if on_bridge and count_q[0] > bridge_length: # 맨 앞 트럭이 다리 끝 지남
            fin_bridge.append(on_bridge.popleft())
            count_q.popleft()
            
        cur_weight = sum(on_bridge)
        if trucks:
            if bridge_length - len(on_bridge) >= 0 and trucks[0] <= weight - cur_weight: # 길이 충족 & 현재 가능 무게보다 가벼운 경우 
                cur_truck = trucks.popleft()
                on_bridge.append(cur_truck)    
                count_q.append(1)
        
        if len(count_q) > 0: # 현재 다리 위 위치
            for i in range(len(count_q)):
                count_q[i] += 1
                

    return time_count