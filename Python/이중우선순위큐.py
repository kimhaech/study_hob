# 두개의 큐를 사용
# 각 최대,최소힙으로 만든다
# 최솟값, 최댓값 삭제 -> 최소힙 pop, 최대힙 pop
# count_len - 삽입될 때 +1 삭제될 때 마다 -1
# 최종으로 남은 힙의 교집합을 구했을 때 남아있는 값이 최종
import heapq
def solution(operations):
    answer = []
    def_heap = [] # 최소힙(기본)
    m_heap = [] # 최대힙
    temp_list = []
    count_len = 0
    
    for val in operations:
        fuc, val = val.split(" ")
        if fuc == "I": # 삽입
            heapq.heappush(def_heap, int(val))
            heapq.heappush(m_heap, -int(val))
            count_len += 1
        else: # 삭제
            if count_len > 0: # 빈 큐가 아닐 때
                if int(val) > 0: # 최댓값 삭제
                    heapq.heappop(m_heap)
                else: # 최솟값 삿제
                    heapq.heappop(def_heap)
                count_len -= 1
    if count_len == 0:
        return [0,0]
    else:
        for v in m_heap:
            temp_list.append(-v)
        temp_answer = list(set(def_heap) & set(temp_list))
        temp_answer.sort()
        answer = [temp_answer[-1],temp_answer[0]]
        
    return answer