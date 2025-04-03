# n = 논문 갯수
# h번 이상 인용 논문의 수가 h개 이상
# h는 논문 갯수 이하 - h <= n
# 
def count_cit(val, arr):
    result = 0 
    for i in arr:
        if i >= val:
            result+=1
    return result
    
def solution(citations):
    answer = 0
    for i in range(len(citations)+1):
        temp = count_cit(i, citations)
        if temp < i:
            return answer
        else:
            answer = i
    return answer