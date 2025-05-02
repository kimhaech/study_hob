from collections import deque

def solution(begin, target, words):
    answer = 0
    visit = {} # 방문 기록용 dict
    next_q = deque()
    
    for word in words: # 방문 기록 dict 초기화
        visit[word] = 0
    
    # 목표 단어가 리스트에 없음
    if target not in words:
        return 0
    
    next_q.append([begin,0])
    while next_q:
        temp_w, cnt = next_q.popleft() # 현재 단어
        if temp_w == target: # 타겟 문자
            answer = cnt
            break
        
        for w in words:
            if compare_func(temp_w, w) and visit[w] == 0: # 비교 시 하나만 다른 경우 and 방문이력 없음
                next_q.append([w,cnt+1])
                visit[w] = 1 # 방문처리       
    
    return answer

# 단어 비교 함수
def compare_func(word1, word2): 
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt == 2: # 다른 단어 수가 2개 이상이 되는 경우
            return False
    return True