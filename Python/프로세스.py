# 두 개의 큐, 그리고 각 큐에 인덱스 값(location 확인용)과 원소값을 넣음
# 하나씩 빼서 최대값과 비교 그리고 문제 로직 그대로 진행
from collections import deque

def solution(priorities, location):
    answer = 0
    ind_list = deque()
    proc_list = deque()
    cur_count = 0
    temp_max = max(priorities)
    
    for i in range(len(priorities)): # 값을 queue에 넣음
        ind_list.append(i) # 좌표값(location)
        proc_list.append(priorities[i]) # 원소의 값
    
    while proc_list:
        ind = ind_list.popleft()
        proc = proc_list.popleft()
        if temp_max > proc: # 현재 값이 우선순위에 밀리는 경우
            ind_list.append(ind)
            proc_list.append(proc)
        else: # 현재 값이 최고 우선순위인 경우
            cur_count += 1
            if ind == location: # 찾고자 하는 위치의 값
                return cur_count
            if proc_list: # 해당 리스트가 비지 않았을 때
                temp_max = max(proc_list)
            
    answer = cur_count
    return answer