# heapq 사용
# 최소 힙으로 만들어서 하나씩 빼서 계산
# 최소 값이 K이상인 경우 종료
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[-1] == 0: # 모든 값이 0인 경우
        return -1
    
    while scoville[0] < K: # 최소값이 K 이하일 때 까지 반복
        if len(scoville) == 1: # 예외 - 다 섞어서 1개 남았는데 K 미만
            return -1
        min_val = heapq.heappop(scoville) # 가장 작은 값
        next_min_val = heapq.heappop(scoville) # 두 번째로 작은 값
        temp_val = min_val + (next_min_val * 2) # 섞기
        heapq.heappush(scoville, temp_val)
        answer += 1
        
    return answer