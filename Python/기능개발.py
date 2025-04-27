# 큐에 작업들을 넣기
# 매 반복 1회 -> 하루
# 각 작업에 개발량을 더하기
# 완료된 작업이 있는지 체크 후 있다면 leftpop -> 추가 검사
# 해당 일의 완료 작업 카운팅 후 1개 이상인 경우 answer에 추가
from collections import deque

def solution(progresses, speeds):
    answer = []
    temp_q = deque()
    temp_sq = deque()
    
    for i in range(len(speeds)):
        temp_q.append(progresses[i])
        temp_sq.append(speeds[i])
        
    while temp_q:
        for i in range(len(temp_q)): # 작업 더하기
            temp_q[i] += temp_sq[i]
            
        temp_count = 0
        
        while temp_q and temp_q[0] >= 100:
            temp_q.popleft()
            temp_sq.popleft()
            temp_count += 1
              
        if temp_count > 0:
            answer.append(temp_count)
            
    return answer